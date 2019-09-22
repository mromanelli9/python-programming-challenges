#!/usr/bin/env python

from typing import Tuple, List

"""
Difficulty: 3

For the 
Write a function in python that computes the number of value crossing events,
which is the number of times a signal crosses a specific value
(crossing value). This is similar to zero crossing detection,
but instead of detecting when the signal changes sign (crosses the zero value)
the function should detect when the signal crosses a user defined value.

ASCII images A, B show examples of value crossing events
where the horizontal line is the user defined crossing value.

Image A:
    /
   /
--+----
 /
/

Image B:
       /
      /
--++++------
 /
/

At the event where a signal takes a value which is the same
as the crossing value at some point or several contiguous points,
but the signal before and after the event stays on the same side
of the crossing value, we do not consider the event as a value crossing event.
So examples C, D are not considered crossing value events.

Image C:
______
  /\
 /  \
/    \

Image D:
_________
  /   \
 /     \
/       \

"""


def signal_crossing(signal: List[float], value: int) -> int:
    """
    Args:
        signal: The signal is described as a list of real numbers.
        value: The crossing value.

    Returns:
         A non-negative integer number that is the number of value crossing events.

    Examples:
        >>> signal_crossing([0.1, 0.2, 3, 4], 3)
        1
        >>> signal_crossing([1, 2, 4, 0.1], 3.4)
        2
        >>> signal_crossing([3, 2.3, 2.1, 2.1, 2.3, 3], 2.1)
        0

    """
    # the signal should be at least of 2 elements to cross a value
    if len(signal) <= 1:
        return 0

    # fist, mark with "-" the values of the signal below the crossing value
    # and with "+" the values above
    signs = []
    for i in range(0, len(signal)):
        if signal[i] < value:
            signs.append("-")
        elif signal[i] > value:
            signs.append("+")

    # then count how many times the markers differ (the signal crossed the value)
    crossed = 0
    for i in range(0, len(signs) - 1):
        if signs[i] != signs[i + 1]:
            crossed += 1

    return crossed
