"""
This module demonstrates basic functionalities including a simple greeting function and a custom exception.

Functions:
- say_hello: Returns a greeting message.
- raise_exception: Raises a custom exception ExampleCustomError.
"""

from .exceptions import ExampleCustomError


def say_hello() -> str:
    """
    Return a greeting message.

    Returns:
        str: A greeting message "hello".
    """
    return "hello"


def raise_exception() -> None:
    """
    Raise the ExampleCustomError custom exception.

    Raises:
        ExampleCustomError: An error indicating a custom exception has occurred.
    """
    raise ExampleCustomError
