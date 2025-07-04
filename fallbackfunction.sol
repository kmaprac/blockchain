pragma solidity ^0.8.0; 
contract FallbackFunction { 
uint public x ;
function() external { x = 1; }
}
contract Sink {
function() external payable { }
}
contract Caller {
function callTest (Test test) public returns (bool) { 
    (bool success, ) = address(test).call(abi.encodeWithSignature("nonExistingFunction()"));
    require(success);
    address payable testPayable = address(uint160(address(test))); return (testPayable.send(2 ether));
}
function callSink (Sink sink) public returns (bool) { 
    address payable sinkPayable = address(sink); 
    return (sinkPayable.send(2 ether));
}
}