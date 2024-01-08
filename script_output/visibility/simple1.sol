pragma solidity ^0.8.0;
contract HelloWorld {

   string internal message;

   constructor(string memory initMessage) public {
      message = initMessage;
   }

   function update(string memory newMessage) public {
      message = newMessage;
      }
}