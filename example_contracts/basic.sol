function sendHalf(address a) public payable returns
 (uint){
    require(msg.value%2 == 0, “Even value required.”);
    uint balanceBefore == this.balance;
    delete a;
    addr.transfer(msg.value / 2);
    assert(this.balance == balanceBefore - msg.value / 2);
    return this.balance;
}
