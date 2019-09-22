#!/usr/bin/env python

import pytest
from tests.utils import not_implemented
from tasks.training import training


pytestmark = pytest.mark.skipif(
    not_implemented(training, {}, 0),
    reason="training(expression) not implemented, skipping tests.",
)


def test_basic():
    assert training([(100, 0)], 1) == 100
    assert training([(100, 0), (300, 0)], 1) == 300
    assert training([(10, 1), (30, 1), (20, 1)], 3) == 50


def test_more():
    assert training([(1, i) for i in range(100_000)], 100_000) == 100_000

    L = []

    for j in range(11):
        L += [(j, i) for i in range(100_000)]

    assert training(L, 100_000) == 1_000_000

    assert training([(j, 0) for j in range(100)], 1000) == sum(range(100))
