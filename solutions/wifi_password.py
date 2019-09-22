#!/usr/bin/env python

"""
Difficulty: 1

Someone told you the password to the WiFi is the N'th fibonacci number. Wanting to
connect to the WiFi you have decided to write an algorithm to figure it out.
N is really large and you don't have all day.
"""

import numpy as np

def wifi_password(n: int) -> int:
    """
    Args:
        n: The number your friend told you.

    Returns:
        The wifi password.

    Examples:
    >>> wifi_password(5)
    5
    >>> wifi_password(0)
    0
    >>> wifi_password(1)
    1
    """
    # Two variables to store F_i and F_{i+1}
    cur_val = 0
    next_val = 1

    # Iteratively look at the two precedent numbers,
    # sum them up, and write the new number.
    for i in range(n):
        (cur_val, next_val) = (next_val, cur_val + next_val)

    # Return F_i
    return cur_val
