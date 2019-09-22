#!/usr/bin/env python

import pytest
from tests.utils import not_implemented
from tasks.signal_crossing import signal_crossing


pytestmark = pytest.mark.skipif(
    not_implemented(signal_crossing, [0], 0),
    reason="signal_crossing(expression) not implemented, skipping tests.",
)


def test_basic():
    assert signal_crossing([0.1, 0.2, 3, 4], 3) == 1
    assert signal_crossing([1, 2, 4, 0.1], 3.4) == 2
    assert signal_crossing([3, 2.3, 2.1, 2.1, 2.3, 3], 2.1) == 0