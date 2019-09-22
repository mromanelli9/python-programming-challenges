#!/usr/bin/env python

import re
from tasks.matmul import transpose, matmul, submatrix, determinant, mul
import numpy
import pytest
from tests.utils import not_implemented


def str_to_array(s):
    return [list(map(int, re.findall(r"-?\s*\d+", row))) for row in s.split("\n")]


@pytest.mark.skipif(
    not_implemented(matmul, [[0]], [[0]]), reason="matmul(X, Y) not implemented"
)
class TestMatrixMultiplication:
    def test_simple_2x2_multiplication(self):
        X = [[1, 2], [3, 4]]
        Y = [[5, 6], [7, 8]]
        result = matmul(X, Y)
        assert result == [[19, 22], [43, 50]]

    def test_identity_2x2_returns_same_value(self):
        X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        Y = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        result = matmul(X, Y)
        assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_simple_4x4_multiplication(self):
        X = [[5, 1, 7, 1], [9, 4, 4, 2], [7, 4, 5, 1], [7, 5, 8, 8]]
        Y = [[6, 8, 2, 4], [1, 5, 8, 1], [8, 7, 1, 4], [8, 6, 7, 9]]
        expected = [
            [95, 100, 32, 58],
            [106, 132, 68, 74],
            [94, 117, 58, 61],
            [175, 185, 118, 137],
        ]
        result = matmul(X, Y)
        assert result == expected

    def test_100x99_with_99x200_multiplication(self):
        numpy.random.seed(sum(ord(c) for c in "Drink more coffee"))
        X = numpy.random.randint(-5, +6, (100, 99)).tolist()
        Y = numpy.random.randint(-5, +6, (99, 200)).tolist()

        expected = numpy.matmul(X, Y).tolist()
        result = matmul(X, Y)
        assert result == expected

    def test_100x100_with_100x_1_multiplication(self):

        numpy.random.seed(420)
        X = numpy.random.randint(-5, +6, (100, 100)).tolist()
        Y = numpy.random.randint(-5, +6, (100, 1)).tolist()

        expected = numpy.matmul(X, Y).tolist()
        result = matmul(X, Y)
        assert result == expected


@pytest.mark.skipif(
    not_implemented(transpose, [[0]]), reason="transpose(X) not implemented"
)
class TestTranspose:
    def test_bigger_100_x_75_transpose(self):

        numpy.random.seed(sum(ord(c) for c in "420 blaze it"))
        X = numpy.random.randint(-5, +6, (100, 75)).tolist()
        expected = numpy.transpose(X).tolist()
        result = transpose(X)
        assert result == expected

    def test_simple_2x2_transpose(self):
        X = [[1, 2], [3, 4]]
        assert transpose(X) == [[1, 3], [2, 4]]


@pytest.mark.skipif(
    not_implemented(submatrix, [[1, 2], [3, 4]], 0, 0),
    reason="submatrix(X, i, j) not imlemented"
)
class TestSubmatrix:
    def test_simple_3x3_submatrix(self):
        s = """ | 1 2 3 |
                | 4 5 6 |
                | 7 8 9 |"""
        X = str_to_array(s)
        assert submatrix(X, 0, 0) == [[5, 6], [8, 9]]
        assert submatrix(X, 0, 1) == [[4, 6], [7, 9]]
        assert submatrix(X, 1, 0) == [[2, 3], [8, 9]]
        assert submatrix(X, 1, 1) == [[1, 3], [7, 9]]
        assert submatrix(X, 2, 0) == [[2, 3], [5, 6]]
        assert submatrix(X, 2, 1) == [[1, 3], [4, 6]]

    def test_4x4_submatrix(self):
        s = """ |  1  2  3  4 |
                |  5  6  7  8 |
                |  9 10 11 12 |
                | 13 14 15 16 | """
        X = str_to_array(s)
        assert submatrix(X, 0, 0) == [[6, 7, 8], [10, 11, 12], [14, 15, 16]]
        assert submatrix(X, 1, 2) == [[1, 2, 4], [9, 10, 12], [13, 14, 16]]


@pytest.mark.skipif(
    not_implemented(determinant, [[0]]), reason="determinant(X) not implemented"
)
class TestDeterminant:
    def test_simple_2x2_determinant(self):
        s = """ | 1 2 |
                | 3 4 |"""
        X = str_to_array(s)

        assert numpy.isclose(determinant(X), -2.0)

    def test_simple_3x3_determinant(self):
        s = """ | 1 2 3 |
                | 4 5 6 |
                | 7 8 9 |"""
        X = str_to_array(s)

        assert numpy.isclose(determinant(X), 0)

        s = """|  4  2  1 |
               | -1 12  7 |
               |  5 14 -2 |"""
        X = str_to_array(s)

        assert numpy.isclose(determinant(X), -496)

    def test_5x5_determinant(self):
        numpy.random.seed(1234)
        X = numpy.random.randn(5, 5).tolist()
        expected = 7.595557255272725
        assert numpy.isclose(determinant(X), expected, rtol=1e-5)


@pytest.mark.skipif(
    not_implemented(matmul, [[0]], [[0]]), reason="matmul(X, Y) not implemented"
)
@pytest.mark.skipif(
    not_implemented(determinant, [[0]]), reason="determinant(X) not implemented"
)
@pytest.mark.skipif(
    not_implemented(submatrix, [[1, 2], [3, 4]], 0, 0),
    reason="submatrix(X, i, j) not imlemented"
)
def test_solve_linear_system_and_get_back_to_earth():
    # We need to solve this linear system in order to fly back to the Earth.
    # Don't ask how, it just works.
    s = """| 1  1  1 |
           | 0  2  5 |
           | 2  5 -1 |"""
    X = str_to_array(s)
    Y = [[6], [-4], [27]]

    det = determinant(X)
    I, J = len(X), len(X[0])

    def cofactor(X, i, j):
        sgn = (-1) ** (i + j)
        minor = determinant(submatrix(X, i, j))
        return sgn * minor

    cofactor_matrix = [[cofactor(X, i, j) for j in range(J)] for i in range(I)]
    adjucate_matrix = transpose(cofactor_matrix)
    det = determinant(X)

    X_inverse = mul(adjucate_matrix, 1 / det)
    result = matmul(X_inverse, Y)
    expected = [[5], [3], [-2]]

    assert numpy.isclose(result, expected).all()
    print(
        "Congratulations! You just solved the linear system and can fly "
        "back to Earth :-)"
    )
