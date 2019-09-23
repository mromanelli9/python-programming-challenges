#!/usr/bin/env python

"""
Difficulty: 1

To increase their Google search rating, Ernst & Young wants to automatically
post their company name over the internet. But the engineers at Ernst & Young
suspects that Google has filters in place for when bots just spam
the same string over and over.

Therefore, they want you to implement the function below.
It takes three numbers. These three numbers will chose the string,
using a quite simple pattern.

- If the number is divisible by the div1, the string should be Ernst.
- If the number is divisible by the div2, the string should be Young.
- If the number is divisble by both div1 and div2, the string
    should be Ernst & Young.
- If the number is divisible by neither, simply return the number as a string.

"""


def marketing(number: int, div1: int, div2: int) -> str:
    """
    Args:
        number: The number to check
        div1: The first divisor
        div2: The second divisor

    Returns:
        The correct string.

    Examples:
    >>> marketing(5, 2, 3)
    "5"
    >>> marketing(10, 2, 3)
    "Ernst"
    >>> marketing(15, 3, 5)
    "Ernst & Young"
    >>> marketing(15, 2, 5)
    "Young"
    """
    raise NotImplementedError()