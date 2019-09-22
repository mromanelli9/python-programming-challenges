#!/usr/bin/env python

import pytest
from tests.utils import not_implemented
from tasks.pipes import num_connected_platforms


pytestmark = pytest.mark.skipif(
    # Skip all tests in this module if the function(s) are not implemented
    not_implemented(num_connected_platforms, [False], []),
    reason="num_connected_platforms(expression) not implemented, skipping tests.",
)


def test_basic():
    assert num_connected_platforms([False, True], [(2, 1)]) == 1

    assert num_connected_platforms([False, True, True], [(1, 2), (2, 3)]) == 0

    assert num_connected_platforms([True, False, True], [(3, 2), (2, 1)]) == 2


def test_other():
    assert num_connected_platforms([False, False], [(1, 2), (2, 1)]) == 0

    assert num_connected_platforms([True, True], [(1, 2), (2, 1)]) == 2

    assert num_connected_platforms([True], []) == 1
