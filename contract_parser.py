
import os
import shutil
import glob
from solcx import compile_standard  
class ContractParser():

    def __init__(self, basic_mutations, extra_mutations, remove_line_mutations, payable):
        self.basic_mutations = basic_mutations
        self.extra_mutations = extra_mutations
        self.remove_line_mutations = remove_line_mutations
        self.payable = payable
    
    def read_contract(self, contract_path):
        with open(contract_path, 'r') as f:
            contract = f.read()
            lines = contract.splitlines()
            return lines
    
    def create_tree(self, path):
        
        if os.path.exists("script_output"):
            shutil.rmtree("./script_output", ignore_errors=False)

        file_name = path.split('/')[-1][:-4]

        lines = self.read_contract(path)
        for i, line in enumerate(lines):

            if "//TESTS" in line:
                break

            if line.strip().startswith("//"):
                continue
                

            line = line.split(' ')
            for key, ll in self.basic_mutations.items():
                for value in ll:
                    
                    shouldMutate = False
                    if key == 'int-types' or key == 'bin-arithmetic':
                        if value in line:
                            shouldMutate = True
                    else:
                        if any(value in word for word in line):
                            shouldMutate = True

                    if shouldMutate:
                        list_without_found = ll.copy()
                        list_without_found.remove(value)
        
                        for changer in list_without_found:
                            self.create_mutant_of_type(lines, i, value, changer, key, file_name)
            

            for value in self.remove_line_mutations:
                if any(value in word for word in line):
                    whole_line = ' '.join(line)
                    self.create_mutant_by_removing_line(lines, lines.index(whole_line), 'require_delete_comment', file_name)

            if "payable" in line and self.payable:
                self.create_mutant_of_type(lines, i, "payable", "", "payable", file_name)    
            
            if not self.extra_mutations:
                continue

            for value in self.extra_mutations["shortcut-arithmetic"]:

                if any(value in word for word in line):
                    
                    indexes = [i for i, s in enumerate(line) if value in s]

                    other_value = list(filter(lambda x: x != value, self.extra_mutations["shortcut-arithmetic"]))[0]
                    
                    for index in indexes:
                        mutants = []
                        variable_stripped = ''
                        if line[index].startswith(value):
                            
                            variable_stripped = line[index][2:]
                            if ';' in variable_stripped:
                                variable_stripped = variable_stripped[:-1]
                            mutants.append(variable_stripped + value)
                        else:
                            variable_stripped = line[index][:line[index].find(value)]
                            mutants.append(value + variable_stripped)
                        mutants.append(variable_stripped + other_value)
                        mutants.append(other_value + variable_stripped)
                        self.create_mutans_based_on_list(lines, i, mutants, line[index], "shortcut-arithmetic", file_name)
    
    def create_mutant_by_removing_line(self, lines, line_id, key, file_name):
        lines_to_edit = lines.copy()

        i = line_id
        while ';' not in lines_to_edit[i]:
            i += 1

        lines_to_edit = lines_to_edit[:line_id] + lines_to_edit[i+1:]
        new_contract = '\n'.join(lines_to_edit)
        self.create_mutant_file(key, file_name, new_contract)

    def create_mutans_based_on_list(self, lines, i, mutants, value, key, file_name):
        lines_to_edit = lines.copy()

        if ';' in value:
            value = value[:-1]
        
        for mutant in mutants:
            lines_to_edit[i] = lines[i]
            lines_to_edit[i] = lines_to_edit[i].replace(value, mutant)
            new_contract = '\n'.join(lines_to_edit)
            self.create_mutant_file(key, file_name, new_contract)
    
    def create_mutant_of_type(self, lines, i, value, changer, key, file_name):

        lines_to_edit = lines.copy()
        lines_to_edit[i] = lines_to_edit[i].replace(value, changer)

        new_contract = '\n'.join(lines_to_edit)
        self.create_mutant_file(key, file_name, new_contract)
    
    def create_mutant_file(self, key, file_name, new_contract):

        if not os.path.exists(f"script_output/{key}"):
            os.makedirs(f"script_output/{key}")

        dir_size = len(os.listdir(f"script_output/{key}")) + 1

        with open(f"script_output/{key}/{file_name}{dir_size}.sol", "w") as output_file:
            output_file.write(new_contract)
    
    def delete_mutants(self, directory):
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
            print("DELETED "+  file + " DUE TO COMPILATION ERRORS")   
        return mutants

# def read_contract(contract_path):
#     with open(contract_path, 'r') as f:

#         contract = f.read()
#         lines = contract.splitlines()
#         return lines

# basic_mutations = {
#     "state": ["view", "pure"],
#     "visibility": ["internal", "external", "public", "private"],
#     "data-location": ["storage", "memory"],
#     "int-types": ["int", "int8", "int32", "int64", "int128", "int256",
#                   "uint", "uint8", "uint32", "uint64", "uint128", "uint256"],
#     "math-functions": ["addmod", "mulmod"],
#     "address-variable": ["block.coinbase", "msg.sender", "tx.origin"],
#     "ether-units": ["wei", "finney", "szabo", "ehter"],
#     "time-units": ["seconds", "minutes", "hours", "days", "weeks"],
#     "bin-arithmetic": ["+", "-", "*", "/", "%"],
#     "relational-operator": [">=", "<=", "==", "!=", ">", "<"],
#     "bin-conditiona": ["&&", "||", "&", "|"],
#     "shortcut-asignment": ["+=", "-=", "*=", "/=", "&="]
# }
# extra_mutations = {
#     "shortcut-arithmetic": ["++", "--"]
# }
# def create_tree(path):

#     file_name = path.split('/')[-1][:-4]

#     lines = read_contract(path)
#     for i, line in enumerate(lines):
#         if line.strip().startswith("//"):
#             continue

#         line = line.split(' ')
#         for key, ll in basic_mutations.items():
#             for value in ll:
                
#                 if value in line:

#                     list_without_found = ll.copy()
#                     list_without_found.remove(value)
    
#                     for changer in list_without_found:
#                         create_mutant_of_type(lines, i, value, changer, key, file_name)
        
#         for value in extra_mutations["shortcut-arithmetic"]:

#             if any(value in word for word in line):
                
#                 indexes = [i for i, s in enumerate(line) if value in s]

#                 other_value = list(filter(lambda x: x != value, extra_mutations["shortcut-arithmetic"]))[0]
                
#                 for index in indexes:
#                     mutants = []
#                     variable_stripped = ''
#                     if line[index].startswith(value):
                        
#                         variable_stripped = line[index][2:]
#                         if ';' in variable_stripped:
#                             variable_stripped = variable_stripped[:-1]
#                         mutants.append(variable_stripped + value)
#                     else:
#                         variable_stripped = line[index][:line[index].find(value)]
#                         mutants.append(value + variable_stripped)

#                     mutants.append(variable_stripped + other_value)
#                     mutants.append(other_value + variable_stripped)
#                     create_mutans_based_on_list(lines, i, mutants, line[index], "shortcut-arithmetic", file_name)

#         if "payable" in line:
#             create_mutant_of_type(lines, i, "payable", "", "payable", file_name)        

# def create_mutans_based_on_list(lines, i, mutants, value, key, file_name):
#     lines_to_edit = lines.copy()

#     if ';' in value:
#         value = value[:-1]
    
#     for mutant in mutants:
#         lines_to_edit[i] = lines[i]
#         lines_to_edit[i] = lines_to_edit[i].replace(value, mutant)
#         new_contract = '\n'.join(lines_to_edit)
#         create_mutant_file(key, file_name, new_contract)

# def create_mutant_of_type(lines, i, value, changer, key, file_name):

#     lines_to_edit = lines.copy()
#     lines_to_edit[i] = lines_to_edit[i].replace(value, changer)

#     new_contract = '\n'.join(lines_to_edit)
#     create_mutant_file(key, file_name, new_contract)

# def create_mutant_file(key, file_name, new_contract):

#     if not os.path.exists(f"script_output/{key}"):
#         os.makedirs(f"script_output/{key}")

#     dir_size = len(os.listdir(f"script_output/{key}")) + 1

#     with open(f"script_output/{key}/{file_name}{dir_size}.sol", "w") as output_file:
#         output_file.write(new_contract)

# def delete_mutants(directory):
#     all_files=0
#     for subdir, dirs, files in os.walk(directory):
#         to_delete=[]
#         for file in files:
#             all_files+=1
#             filepath = subdir + os.sep + file
#             if filepath.endswith(".sol"):
#                 with open(filepath,"r") as file:
#                     simple_storage_file = file.read()
#             try:
#                 compiled_sol = compile_standard(
#                     {
#                         "language": "Solidity",
#                         "sources": {"contract.sol": {"content": simple_storage_file}},
#                         "settings": {
#                             "outputSelection": {
#                                 "*": {
#                                     "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
#                                 }
#                             }
#                         },
#                     },
#                     solc_version="0.8.0",
#                 )
#                 file.close()
#             except:
#                 to_delete.append(filepath)
#                 file.close()
#     mutants=all_files-len(to_delete)
#     for file in to_delete:
#         os.remove(file)
#         print("DELETED"+  file + "DUE TO COMPILATION ERRORS")   
#     return mutants