#!/usr/bin/env python

from typing import List, Tuple

"""
Difficulty: 4

A group of executives at a large oil company had gone to a conference about ML. After
hearing that it "could learn like a human" they decided to fire all their Geologists
and Geophysicists. They were replaced with a neural network they named Fred. In the
beginning Fred looked great. He was finding oil deposits everywhere. The executives
ordered the building of a lot of new oil platforms following this. After having spent
all their money it became apparent that something was wrong. There was no oil or gass
underneath most of the newly built oil platforms. The executives stopped all current
projects.

This left them with a problem. Not all the pipes to shore were finished, so they are
not sure which of the platforms are actually connected to shore. You are brought on as
a consultant to find the extent of the problem. Being a good consultant you know that
platform 1 is already connected to shore.
"""


def num_connected_platforms(platforms: List[bool], pipes: List[Tuple[int, int]]) -> int:
    """
    Args:
        platforms:  A list booleans. Each boolean signifies whether the platform is
            currently producing oil.
        pipes: A list of tuples, specifying that there is a pipe going from platform a
            to platform b. Pipes only go in one direction.

    Notes:
        The list is 1 indexed. See the `Examples` section for illustration. Platfrom 1
        is connected to shore.

    Returns:
        The number of oil platforms (which produces oil) that are connected to shore.

    Examples:
        >>> platforms([False, True], [(2, 1)])
        1
        >>> platforms([False, True, True, True], [(3, 2), (4, 3)])
        0
        >>> platfroms([True, False, True], [(3, 2), (2, 1)])
        2

    """
    raise NotImplementedError()






