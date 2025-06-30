pragma solidity ^0.8.0; 

contract Function {
    function getResult() public view returns (uint product, uint sum){ 
        uint a = 11;
        uint b = 20; 
        product = a * b; 
        sum = a + b;
    }
}