from solcx import install_solc
from contract_parser import *
from slither_testing import slither_test
from echidna_testing import echidna_test
import os
import time

# if os.path.exists("script_output"):
#     shutil.rmtree("./script_output", ignore_errors=False)

path_to_contract="./example_contracts/lock.sol"
time.sleep(3)

parser = ContractParser()
parser.create_tree(path_to_contract)

warning_num,eror_num,calls_num,length=slither_test(path_to_contract)

install_solc("0.8.0")

if not os.path.exists(f"script_output"):
    os.makedirs(f"script_output")

directory = "./script_output"

# mutants = delete_mutants(directory)
mutants = parser.delete_mutants(directory)
print("THERE ARE " + str(mutants) + " MUTANTS LEFT")
time.sleep(2)

killed=0

# ECHIDNA TESTS
# for subdir, dirs, files in os.walk(directory):
#     for file in files:
#         filepath = subdir + os.sep + file
#         if filepath.endswith(".sol"):
#             print("TESTING :"+ filepath)
#             length=echidna_test(filepath)
#             if length-og_len>10:
#                 print("KILLED: ")
#                 killed+=1
#             else:
#                 print("PASSED")
# SLITHER TESTING

for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".sol"):
            print("TESTING :"+ filepath)
            warning_mutant,error_mutant,calls_mutant,len_mutant=slither_test(filepath)
            if abs(warning_num-warning_mutant)>0 or abs(eror_num-error_mutant)>0 or abs(calls_num-calls_mutant)>0:
                print("KILLED: " +str(abs(warning_num-warning_mutant)) + " WARNINGS FOUND, " +  str(abs(error_mutant - eror_num)) + " ERRORS FOUND, "+ str( abs(calls_mutant - calls_num)) + " CALLS FOUND" )
                killed+=1
            else:
                print("PASSED")

print("MUTANTS SURVIVED:"+ str(mutants-killed))
print("MUTANTS KILLED:"+ str(killed))
print("MUTATION SCORE IS: " + str((killed/mutants )* 100)  + "%")
