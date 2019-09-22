#!/usr/bin/env python

from typing import List

"""
Difficulty: 3

You are running a large software company specializing in web development.
You have k employees working n hours a week each. A client has requested that x
hours should be spent on a project each week. They want the developers to devote all
their time to the project. You want to know whether there is a combination of developers
that gives the exact amount of hours requested.
"""


def exact_hours(hours: List[int], requested_by_client: int) -> bool:
    """
    Args:
        hours: Integers denoting how many hours a given developer is working. The number
            of developers is the same as the length of this array.
        requested_by_client: The number of hours the client is requesting.

    Returns:
        Whether there is a combination of developers that give the exact
        number of hours specified.

    Example:
        >>> print(exact_hours([0, 1, 2], 3))
        True
        >>> print(exact_hours([5, 15, 2, 8, 3, 1], 19))
        True
        >>> print(exact_hours([2, 4, 6, 8], 13))
        False
        >>> print(exact_hours([5], 4))
        False
    """
    raise NotImplementedError()
