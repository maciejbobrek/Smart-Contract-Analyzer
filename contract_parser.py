
import os
import shutil
import glob
from solcx import compile_standard

def read_contract(contract_path):
    with open(contract_path, 'r') as f:

        contract = f.read()
        lines = contract.splitlines()
        # print(os.path.splitext(contract_path)[0])
        return lines

basic_mutations = {
    "state": ["view", "pure"],
    "visibility": ["internal", "external", "public", "private"],
    "data-location": ["storage", "memory"],
    # "int-types": ["int", "int8", "int32", "int64", "int128", "int256",
    #               "uint", "uint8", "uint32", "uint64", "uint128", "uint256"],
    "math-functions": ["addmod", "mulmod"],
    "address-variable": ["block.coinbase", "msg.sender", "tx.origin"],
    "ether-units": ["wei", "finney", "szabo", "ehter"],
    "time-units": ["seconds", "minutes", "hours", "days", "weeks"],
    "bin-arithmetic": ["+", "-", "*", "/", "%"],
    "relational-operator": [">=", "<=", "==", "!=", ">", "<"],
    "bin-conditiona": ["&&", "||", "&", "|"],
    "shortcut-asignment": ["+=", "-=", "*=", "/=", "&="]
}
extra_mutations = {
    "shortcut-arithmetic": ["++", "--"]
}
def create_tree(path):

    file_name = path.split('/')[-1][:-4]

    lines = read_contract(path)
    for i, line in enumerate(lines):

        if line.strip().startswith("//"):
            continue

        line = line.split(' ')
        for key, list in basic_mutations.items():
            for value in list:
                
                if value in line:

                    list_without_found = list.copy()
                    list_without_found.remove(value)
    
                    for changer in list_without_found:
                        create_mutant_of_type(lines, i, value, changer, key, file_name)
        
        for value in extra_mutations["shortcut-arithmetic"]:
            if value in line:
                index = line.index(value)

                other_value = extra_mutations["shortcut-arithmetic"].remove(value)
                mutants = []

                if line[index].startswith(value):
                    
                    variable_stripped = line[index][2:]
                    mutants.append(variable_stripped + value)
                else:
                    variable_stripped = line[index][:-2]
                    mutants.append(value + variable_stripped)

                mutants.append(variable_stripped + other_value)
                mutants.append(other_value + variable_stripped)
                create_mutans_based_on_list(lines, i, index, mutants, "shortcut-arithmetic", file_name)

        if "payable" in line:
            
            create_mutant_of_type(lines, i, "payable", "", "payable", file_name)        

def create_mutans_based_on_list(lines, i, index, mutants, key, file_name):

    lines_to_edit = lines.copy()

    for mutant in mutants:
        lines_to_edit[i][index] = mutant
        new_contract = '\n'.join(lines_to_edit)
        create_mutant_file(key, file_name, new_contract)

def create_mutant_of_type(lines, i, value, changer, key, file_name):

    lines_to_edit = lines.copy()
    lines_to_edit[i] = lines_to_edit[i].replace(value, changer)
    # if value == "payable":
    #     print(lines_to_edit[i])

    new_contract = '\n'.join(lines_to_edit)
    create_mutant_file(key, file_name, new_contract)

def create_mutant_file(key, file_name, new_contract):

    if not os.path.exists(f"script_output/{key}"):
        os.makedirs(f"script_output/{key}")
    dir_size = len(os.listdir(f"script_output/{key}")) + 1

    with open(f"script_output/{key}/{file_name}{dir_size}.sol", "w") as output_file:
        output_file.write(new_contract)

def delete_mutants(directory):
    all_files=0
    for subdir, dirs, files in os.walk(directory):
        to_delete=[]
        for file in files:
            all_files+=1
            filepath = subdir + os.sep + file
            if filepath.endswith(".sol"):
                with open(filepath,"r") as file:
                    simple_storage_file = file.read()
            try:
                compiled_sol = compile_standard(
                    {
                        "language": "Solidity",
                        "sources": {"contract.sol": {"content": simple_storage_file}},
                        "settings": {
                            "outputSelection": {
                                "*": {
                                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                                }
                            }
                        },
                    },
                    solc_version="0.8.0",
                )
                file.close()
            except:
                to_delete.append(filepath)
                file.close()
    mutants=all_files-len(to_delete)
    for file in to_delete:
        os.remove(file)
        print("DELETED"+  file + "DUE TO COMPILATION ERRORS")   
    return mutants