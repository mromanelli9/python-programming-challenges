#!/usr/bin/env python

from typing import Tuple, List

"""
Difficulty: 5

You are a computer science graduate doing an internship for a local bank
that works with large financial datasets. All these datasets are
on a single computer. Your colleague engineers want to run experiments on the computer.
Running an experiment takes exactly one day.

All the experiments are part of the same project. The project ends N days after the
first day. Being really smart you know that the engineer will spend a certain amount
of days collecting training data and that the project has an exact value.

You goal is to find the maximum possible value of the project. The value of the project
is the same as the sum of all the experiments that have been run before the end of the
project.
"""


def training(experiments: List[Tuple[int, int]], last_day: int) -> int:
    """
    Args:
        experiments: First element in the tuple specifies the value of the experiment.
            The second value specifies the day that experiment will be ready.
        last_day: The last day of the project.

    Returns:
        The maximum value of the project, given as the sum of all the experiments run.

    Examples:
        >>> training([(100, 0)], 1)
        100
        >>> training([(100, 0), (300, 0)], 1)
        300
        >>> training([(10, 1), (30, 1), (20, 1)], 3)
        50

    """
    raise NotImplementedError()
