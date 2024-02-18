from contract_parser import *
from mainGUI import logic
import os

basic_mutations = {
"state": ["view", "pure"],
"visibility": ["internal", "external", "public", "private"],
"data-location": ["storage", "memory"],
"int-types": ["int", "int8", "int32", "int64", "int128", "int256",
                "uint", "uint8", "uint32", "uint64", "uint128", "uint256"],
"math-functions": ["addmod", "mulmod"],
"address-variable": ["block.coinbase", "msg.sender", "tx.origin"],
"ether-units": ["wei", "finney", "szabo", "ether"],
"time-units": ["seconds", "minutes", "hours", "days", "weeks"],
"bin-arithmetic": ["+", "-", "*", "/", "%"],
"relational-operator": [">=", "<=", "==", "!=", ">", "<"],
"bin-condition": ["&&", "||", "&", "|"],
"shortcut-asignment": ["+=", "-=", "*=", "/=", "&="]
}
extra_mutations = {
"shortcut-arithmetic": ["++", "--"]
}
remove_line_mutations = ['delete', 'require']



def script(dir_path):
    for subdir, dirs, files in os.walk(dir_path):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".sol"):
                test_contract(filepath)


def test_contract(path):
    new_extra_mutations = dict()
    new_remove_line_mutations = []
    payable = False

    DO_ECHIDNA = False
    DO_SLITHER = True

    values = dict()

    # basic mutations
    for key, val in basic_mutations.items():
        new_basic_mutations = dict()
        new_basic_mutations[key] = val
        parser_basic = ContractParser(new_basic_mutations, new_extra_mutations, new_remove_line_mutations, payable)
        parser_basic.create_tree(path)
        score = logic(parser_basic, path, DO_SLITHER, DO_ECHIDNA)
        values[key] = score
    
    #extra mutations
    new_basic_mutations = dict()
    parser_extra = ContractParser(new_basic_mutations, extra_mutations, new_remove_line_mutations, payable)
    parser_extra.create_tree(path)
    score = logic(parser_extra, path, DO_SLITHER, DO_ECHIDNA)
    values["shortcut-arithmetic"] = score

    #remove line mutations
    for val in remove_line_mutations:
        new_remove_line_mutations = []
        new_remove_line_mutations.append(val)
        parser_remove_line = ContractParser(new_basic_mutations, new_extra_mutations, new_remove_line_mutations, payable)
        parser_remove_line.create_tree(path)
        score = logic(parser_remove_line, path, DO_SLITHER, DO_ECHIDNA)
        values[val] = score

    #payable
    payable = True
    parser_payable = ContractParser(new_basic_mutations, new_extra_mutations, new_remove_line_mutations, payable)
    parser_payable.create_tree(path)
    score = logic(parser_payable, path, DO_SLITHER, DO_ECHIDNA)
    values['payable'] = score

    #contract with all
    parser_full = ContractParser(basic_mutations, extra_mutations, remove_line_mutations, payable)
    parser_full.create_tree(path)
    score = logic(parser_full, path, DO_SLITHER, DO_ECHIDNA)
    values['all_mutagens'] = score
    save_dict_to_file(values, path)

def save_dict_to_file(values, file_name):

    if not os.path.exists(f"scores_script"):
        os.makedirs(f"scores_script")
    new_file_name = file_name.split('\\')[1][:-4] + '.txt'

    with open(f'scores_script/{new_file_name}', 'w+') as f:
        s = ''
        for key, val in values.items():
            s += f'{key}: {val}%\n'
        f.write(s)
        

dir_path = 'example_contracts'
script(dir_path)