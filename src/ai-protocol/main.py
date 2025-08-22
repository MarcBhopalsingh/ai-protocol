#!/usr/bin/env python3
"""
Hello World Python Project

A simple demonstration of Python programming basics.
"""

def say_hello(name: str = "World") -> str:
    """
    Returns a personalized greeting message.
    
    Args:
        name (str): The name to greet. Defaults to "World".
        
    Returns:
        str: The greeting message.
    """
    return f"Hello, {name}!"

def main():
    """Main function to demonstrate the hello world functionality."""
    # Basic hello world
    print(say_hello())
    
    # Personalized greeting
    print(say_hello("Python Developer"))
    
    # Interactive greeting
    user_name = input("Enter your name (or press Enter for default): ").strip()
    if user_name:
        print(say_hello(user_name))
    else:
        print(say_hello())

if __name__ == "__main__":
    main()
