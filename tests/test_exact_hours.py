#!/usr/bin/env python

import pytest

from tests.utils import not_implemented
from tasks.exact_hours import exact_hours


pytestmark = pytest.mark.skipif(
    # Skip all tests in this module if the function(s) are not implemented
    not_implemented(exact_hours, [], 0),
    reason="exact_hours(numbers) not implemented, skipping tests.",
)


def test_simple_lists():
    assert exact_hours([0, 1, 2, 3, 4], 0)
    assert not exact_hours([15, 25, 35, 45], 16)
    assert exact_hours([1, 2, 3, 4, 5], 15)
    assert not exact_hours([2, 4, 8, 16, 32], 25)


@pytest.mark.timeout(10)
def test_long_lists():
    assert exact_hours([i for i in range(50)], 805)
    assert not exact_hours([1, 3, 8, 5, 6, 13, 19, 7, 11, 19, 58, 108], 259)
    assert exact_hours([1, 3, 8, 5, 6, 13, 19, 7, 11, 19, 58], 117)
    assert not exact_hours([0, 4, 8, 12, 6, 13, 48, 7, 11, 19, 58, 18, 52, 2, 41], 294)
