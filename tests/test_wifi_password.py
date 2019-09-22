#!/usr/bin/env python

import pytest
from tests.utils import not_implemented
from tasks.wifi_password import wifi_password


pytestmark = pytest.mark.skipif(
    # Skip all tests in this module if the function(s) are not implemented
    not_implemented(wifi_password, 0),
    reason="wifi_password(n) not implemented, skipping tests.",
)


def test_small_fib():
    assert wifi_password(7) == 13
    assert wifi_password(10) == 55
    assert wifi_password(0) == 0
    assert wifi_password(1) == 1
    assert wifi_password(15) == 610


@pytest.mark.timeout(5)
def test_medium_fib():
    assert wifi_password(40) == 102334155
    assert wifi_password(60) == 1548008755920


@pytest.mark.timeout(5)
def test_large_fib():
    fib_1000 = (
        "434665576869374564356885276750406258025646605173717804024817290895365554179"
        "490518904038798400792551692959225930803226347752096896232398733224711616429"
        "96440906533187938298969649928516003704476137795166849228875"
    )
    fib_1234 = (
        "347746739180370201052517440604335969788684934927843710657352239304121649686"
        "845967975636459392453053377493026875020744760145842401792378749321113719919"
        "618588095724485583919541019961884523908359133457357334538791778480910430756"
        "107407761555218113998374287548487"
    )
    assert wifi_password(1000) == int(fib_1000)
    assert wifi_password(1234) == int(fib_1234)
