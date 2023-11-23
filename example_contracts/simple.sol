pragma solidity ^0.6.0;
contract HelloWorld {

   string public message;

   constructor(string memory initMessage) public {
      message = initMessage;
   }

   function update(string memory newMessage) public {
      message = newMessage;
      }
}