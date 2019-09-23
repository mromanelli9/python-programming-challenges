#!/usr/bin/env python

import pytest
from tests.utils import not_implemented
from tasks.marketing import marketing

pytestmark = pytest.mark.skipif(
    # Skip all tests in this module if the function(s) are not implemented
    not_implemented(marketing, 1, 1, 1),
    reason="marketing(expression) not implemented, skipping tests.",
)


def test_marketing():
    assert marketing(100, 10, 10) == "Ernst & Young"
    assert marketing(11, 2, 3) == "11"
    assert marketing(12, 2, 3) == "Ernst & Young"
    assert marketing(13, 2, 3) == "13"
    assert marketing(14, 2, 3) == "Ernst"
    assert marketing(15, 21, 31) == "15"
    assert marketing(15, 21, 5) == "Young"
