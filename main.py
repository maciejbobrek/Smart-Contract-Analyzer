from eth_utils import address
from solcx import compile_standard, install_solc
from dotenv import load_dotenv
import json
from contract_parser import *
import antlr4
import os
install_solc("0.6.0")


shutil.rmtree("./script_output", ignore_errors=False)
create_tree("./example_contracts/lock.sol")
#create_tree("./example_contracts/lock.sol")
#create_tree("./example_contracts/simple.sol")
directory = "./script_output"

for subdir, dirs, files in os.walk(directory):
    to_delete=[]
    for file in files:
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
                solc_version="0.6.0",
            )
            file.close()
        except:
            to_delete.append(filepath)
            file.close()

for filepath in to_delete:
    print("Deleted " + filepath + ": compilation errors")
    os.remove(filepath)