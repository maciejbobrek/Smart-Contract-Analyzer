
import os
import shutil

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

lines, contract = read_contract("example_contracts\lock.sol")
shutil.rmtree("script_output", ignore_errors=False)

for i, line in enumerate(lines):
    if line.strip().startswith("//"):
        continue
    line = line.split(' ')
    # print(line)
    for key, list in mutations.items():
       
        for value in list:
            
            if value in line:

                list_without_found = list
                list_without_found.remove(value)
  

                for changer in list_without_found:
                    lines_to_edit = lines.copy()
                    lines_to_edit[i] = lines_to_edit[i].replace(value, changer)

                    new_contract = '\n'.join(lines_to_edit)
                    # print(i, value, lines_to_edit[i])
                    # print(new_contract)
                    # exit(0)
                    # line_to_edit.replace(value, changer)

                    if not os.path.exists(f"script_output/{key}"):
                        os.makedirs(f"script_output/{key}")
                    
                    files = os.listdir(f"script_output/{key}")



                    dir_size = len(os.listdir(f"script_output/{key}")) + 1
                    # print(dir_size)
                    # print(f"script_output/{key}/changed{dir_size}.sol")
                    with open(f"script_output/{key}/changed{dir_size}.sol", "w") as output_file:
                        # print(f"File {key}/changed{dir_size}.sol created")
                        output_file.write(new_contract)
                        output_file.close()



    # whole_file = '\n'.join(lines)

    # if not os.path.exists("script_output"):
    #     os.makedirs("script_output")

    # with open("script_output/file1.sol", 'w') as out:
    #     out.write(whole_file) 