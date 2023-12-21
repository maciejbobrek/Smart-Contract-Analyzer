from eth_utils import address
from solcx import compile_standard, install_solc
# from dotenv import load_dotenv
import json
from contract_parser import *
import antlr4
import os
import subprocess
import time

path_to_contract="./example_contracts/test.sol"
time.sleep(2)
shutil.rmtree("./script_output", ignore_errors=False)
create_tree(path_to_contract)


result = subprocess.run(['slither',path_to_contract], 
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)

length=len(result.stderr.decode())
install_solc("0.8.0")

if not os.path.exists(f"script_output"):
    os.makedirs(f"script_output")



#create_tree("./example_contracts/lock.sol")
#create_tree("./example_contracts/simple.sol")
directory = "./script_output"

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

time.sleep(2)

killed=0
for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".sol"):
            print("TESTING :"+ filepath)
            result = subprocess.run(['slither',filepath], 
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            mutant_length=len(result.stderr.decode())
            if mutant_length-length>500:
                print("KILLED")
                killed+=1
            else:
                print("PASSED")

print("MUTANTS SURVIVED:"+ str(mutants-killed))
print("MUTANTS KILLED:"+ str(killed))
print("MUTATION SCORE IS: " + str((killed/mutants )* 100)  + "%")