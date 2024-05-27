"""
This test module provides unit tests for the Template Python Package module using pytest.

It includes tests for versioning and a couple of example tests.
"""

from typing import Optional

import importlib.metadata
import pytest

from wolfsoftware.template_package_importable import raise_exception, say_hello, ExampleCustomError


def test_version() -> None:
    """
    Test to ensure the version of the Package is set and not 'unknown'.

    This test retrieves the version of the package using importlib.metadata and asserts that the version
    is not None and not 'unknown'.
    """
    version: Optional[str] = None

    try:
        version = importlib.metadata.version('wolfsoftware.template_package_importable')
    except importlib.metadata.PackageNotFoundError:
        version = None

    assert version is not None, "Version should be set"  # nosec: B101
    assert version != 'unknown', f"Expected version, but got {version}"  # nosec: B101


def test_say_hello() -> None:
    """
    Test the say_hello function to ensure it returns the expected greeting message.

    This test calls the say_hello function and asserts that the returned value is 'hello'.
    """
    hello: str = say_hello()

    assert hello == 'hello', f"Expected 'hello', but got {hello}"  # nosec: B101


def test_custom_exception() -> None:
    """
    Test the raise_exception function to ensure it raises the ExampleCustomError with the default message.

    This test uses pytest.raises to assert that calling raise_exception raises the ExampleCustomError
    with the message "A default error message.".
    """
    with pytest.raises(ExampleCustomError, match="A default error message."):
        raise_exception()
