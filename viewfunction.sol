pragma solidity ^0.8.0;

contract ViewFunction { 
    uint num1 = 2;
    uint num2 = 4;
function getResult(
) public view returns(
    uint product, uint sum) {
    uint num1 = 10;
    uint num2 = 16;
    product = num1 * num2;
    sum = num1 + num2;
}
}