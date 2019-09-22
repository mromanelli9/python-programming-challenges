#!/usr/bin/env python

"""
Difficulty: 2

You are a developer that really loves Lisp (the programming language). Using only
notepad you have implemented a huge expression to try to find the faults and horizons in
a dataset.  Given that you don't have a linter, you are not sure whether your
expression is valid. Therefore you decided to implement an algorithm to check if every
parenthesis has the appropriate closing bracket.
"""


def is_valid_lisp(expression: str) -> bool:
    """
    Args:
        expression: Your expression as a string. Will only contain lower case letters,
            spaces and parenthesis.

    Returns:
        Whether the expression is valid. You can assume it is valid if every
        parenthesis has the appropriate closing parenthesis.

    Example:
        >>> print(is_balanced("(("))
        False
        >>> print(is_balanced("(()))("))
        False
        >>> print(is_balanced("()"))
        True
        >>> print(is_balanced("(h(e)l(l)o)"))
        True
    """
    raise NotImplementedError()


