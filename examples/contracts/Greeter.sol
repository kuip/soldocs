pragma solidity ^0.4.17;

contract Greeter {
    string public greeting;

    event GreetSent(address indexed sender, string message, address indexed receiver);

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

    function emitGreeting(address receiver) public {
        GreetSent(msg.sender, greeting, receiver);
    }

    /// @notice Function for greeting people.
    /// @return Return the greeting.
    function greet() public constant returns (string) {
        return greeting;
    }
}
