
import os
import shutil
import glob

def read_contract(contract_path):
    with open(contract_path, 'r') as f:

        contract = f.read()
        lines = contract.splitlines()
        return lines, contract

mutations = {
    "state": ["view", "pure"],
    "visibility": ["internal", "external", "public", "private"],
    #data location
    #variable types
    # "payable": ["payable", ""],
    #many more...
    "bin-arithmetic": ["+", "-", "*", "/", "%"],
    # "shortcut-arithmetic": [" ++", ""]
    "relational-operator": [">=", "<=", "==", "!=", ">", "<"],
    "bin-conditiona": ["&&", "||", "&", "|"],
    "shortcut-asignment": ["+=", "-=", "*=", "/=", "&="]
}



def create_tree(path):
    lines, contract = read_contract(path)
    for i, line in enumerate(lines):
        if line.strip().startswith("//"):
            continue
        line = line.split(' ')
        for key, list in mutations.items():
        
            for value in list:
                
                if value in line:

                    list_without_found = list
                    list_without_found.remove(value)
    

                    for changer in list_without_found:
                        lines_to_edit = lines.copy()
                        lines_to_edit[i] = lines_to_edit[i].replace(value, changer)

                        new_contract = '\n'.join(lines_to_edit)

                        if not os.path.exists(f"script_output/{key}"):
                            os.makedirs(f"script_output/{key}")
                        
                        files = os.listdir(f"script_output/{key}")

                        dir_size = len(os.listdir(f"script_output/{key}")) + 1
                        with open(f"script_output/{key}/changed{dir_size}.sol", "w") as output_file:
                            output_file.write(new_contract)