//SPDX-License-Identifier:MIT
pragma solidity ^0.8.9;

interface IERC20 {

    event Transfer(address indexed from, address indexed to, uint256 value);


    event Approval(address indexed owner, address indexed spender, uint256 value);

    function totalSupply() external view returns (uint256);


    function balanceOf(address account) external view returns (uint256);

    function transfer(address to, uint256 amount) external returns (bool);


    function allowance(address owner, address spender) external view returns (uint256);


    function approve(address spender, uint256 amount) external returns (bool);

    function transferFrom(address from, address to, uint256 amount) external returns (bool);
}

contract Vulnerability {
    address private USDC = 0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48;
    mapping(address => uint256) public balances;
    uint256 public lotteryWinningNumber;
    address public owner;

    constructor(){
        owner = msg.sender;
    }


    function fund_reached() public view returns (bool) {
        return address(this).balance == 100 ether;
    }

    function USDCTransfer(
        address _from,
        address _to,
        uint256 _amount
    ) public {
        IERC20(USDC).transferFrom(_from, _to, _amount);
    }

    function kill() public {
        selfdestruct(payable(msg.sender));
    }

    function delegate(address _to, bytes memory _data) public {
        (bool result, ) = _to.delegatecall(_data);
    }

    function withdraw(uint256 _amount) public {
        if (balances[msg.sender] >= _amount) {
            (bool result, ) = msg.sender.call{value: _amount}("");
            require(result, "Could not transfer");
            balances[msg.sender] -= _amount;
        }
    }

    function winLottery() external{
      lotteryWinningNumber = uint256(block.timestamp) % 10;
    }

    uint256 amt;

    function divideBeforeMultiply(uint256 a, uint256 b, uint256 c) public{
        amt = (a / b) * c;
    }

    function txOriginExploit(uint256 _amount) public{
        require(tx.origin == owner);
        withdraw(_amount);
    }


    function transferMoney() payable public{
        address to;
        (bool result, ) = to.call{value: address(this).balance}("");
        require(result, "Could not transfer");
    }


    uint[1] public x; // storage

    function f() public {
        f1(x); // update x
        f2(x); // do not update x
    }

    function f1(uint[1] storage arr) internal { // by reference
        arr[0] = 1;
    }

    function f2(uint[1] memory arr) internal pure{ // by value
        arr[0] = 2;
    }
}