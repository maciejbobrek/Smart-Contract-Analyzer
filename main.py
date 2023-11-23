import numpy as np
import solidity




with open("./example_contracts/lock.sol", "r") as file:
    simple_storage_file = file.read()