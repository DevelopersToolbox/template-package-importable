"""
This module defines custom exceptions for the importable template package.

Classes:
- ExampleCustomError: A custom exception class with a default error message.
"""


class ExampleCustomError(Exception):
    """
    A custom exception class with a default error message.

    Attributes:
        message (str): The error message for the exception.
    """

    def __init__(self, message: str = "A default error message.") -> None:
        """
        Initialize the ExampleCustomError with an optional error message.

        Args:
            message (str): The error message for the exception. Defaults to "A default error message.".
        """
        super().__init__(message)
