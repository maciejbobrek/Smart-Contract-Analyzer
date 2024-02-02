
    pragma solidity ^0.8.0;

    contract Lock {
        uint public unlockTime;

        mapping(address => uint256) public balances;

        event Withdrawal(uint amount, uint when);

        constructor(uint _unlockTime) payable {
            require(
                block.timestamp < _unlockTime,
                "Unlock time should be in the future"
            );

            unlockTime = _unlockTime;
        }

        function withdraw(uint amount) public {
            uint bal = balances[msg.sender];
            require(block.timestamp >= unlockTime, "You can't withdraw yet");
            require(amount > 0, "Nothing to withdraw");
            (bool sent,) = address(msg.sender).call{value: amount}("");
            require(sent);
            emit Withdrawal(address(this).balance, block.timestamp);

            balances[msg.sender] += amount;
        }
    }