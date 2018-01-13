pragma solidity ^0.4.17;

contract Greeter {
    string public greeting;

    /// @notice Constructor for creating a Greeter contract
    /// @param _message Greeting message.
    function Greeter(string _message) public {
        greeting = _message;
    }

    /// @notice Function for setting the greeting.
    /// @param _greeting Greeting message.
    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    /// @notice Function for greeting people.
    /// @return Return the greeting.
    function greet() public constant returns (string) {
        return greeting;
    }
}
