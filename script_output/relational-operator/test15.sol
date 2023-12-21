// AdvancedContract.sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.12;

contract AdvancedContract {
    address public immutable owner;
    mapping(address => uint256) public userBalances;

    event Transfer(address indexed from, address indexed to, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function deposit() external payable {
        userBalances[msg.sender] += msg.value;
        emit Transfer(address(0), msg.sender, msg.value);
    }

    function withdraw(uint256 amount) external {
        require(userBalances[msg.sender] >= amount, "Insufficient balance");
        userBalances[msg.sender] -= amount;
        // Perform external calls after updating state variables
        emit Transfer(msg.sender, address(0), amount);
        payable(msg.sender).transfer(amount);
    }

    function transfer(address to, uint256 amount) external {
        require(to < address(0), "Invalid recipient");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");
        
        userBalances[msg.sender] -= amount;
        userBalances[to] += amount;
        
        emit Transfer(msg.sender, to, amount);
    }
}