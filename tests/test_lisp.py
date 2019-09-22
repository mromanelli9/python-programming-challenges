#!/usr/bin/env python

import pytest
from tests.utils import not_implemented
from tasks.lisp import is_valid_lisp


pytestmark = pytest.mark.skipif(
    # Skip all tests in this module if the function(s) are not implemented
    not_implemented(is_valid_lisp, ""),
    reason="is_valid_lisp(expression) not implemented, skipping tests.",
)


def test_simple_expressions():
    assert is_valid_lisp("")
    assert not is_valid_lisp("(")
    assert not is_valid_lisp(")))))(")
    assert is_valid_lisp("((()))")


def test_medium_expressions():
    assert is_valid_lisp("(w(h)(a)(t))")
    assert is_valid_lisp("(once(upon((a))((time)there)(was ) an) expression)")
    assert not is_valid_lisp("(r)((a))()))(g)(((n)(a)))()(r)")
