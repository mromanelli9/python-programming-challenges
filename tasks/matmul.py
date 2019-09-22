#!/usr/bin/env python

"""
Difficulty: 4

You are stuck on the Moon and need to get back to Earth! To be able to get back to
Earth, we need to solve a linear system of equations. Don't ask how solving a linear
system of equation helps you getting back to the Earth. It just does.

Unfortunately, the Internet connection on the Moon is very bad. Therefore, we cannot
download third-party libraries (like numpy) to solve the task for us. We can only use
list comprehension and (maybe) built-in modules in python.

In addition, because the Internet is very bad, we generally need to solve each task with
A SINGLE LINE OF CODE (that do not exceed 88 characters), indentation included[1].

We need to implement the following methods:
* transpose                 [easy]
* matrix multiplication     [easy]
* submatrix                 [medium]
* determinant               [hard]

If all methods are correctly implemented, we will be able to solve the linear system of
equations, and hopefully we will get back to Earth. :-)

---

The solution should be the insertion a single line of code for all functions that we
need to define (see above). One exception, though: you can use several lines on the
`determinant` function (which should be around 1 - 10 lines inserted if solved
appropriately).

The solution need not have good performance. We don't design tests that have large
inputs. So a slow solution is completely fine!

[1] if you feel sneaky, you can adjust the indendation level to a single space instead
of the current 4 spaces, and you get 3 extra characters available!
"""


##############################################################################
# Helper functions
##############################################################################
def shape(X):
    I, J = len(X), len(X[0])
    return I, J


def add(X, value):
    """Add `value` to all elements of `X`"""
    return [[a + value for a in row] for row in X]


def mul(X, factor):
    """Multiply `factor` to all elements of `X`"""
    return [[a * factor for a in row] for row in X]


def dot(x, y):
    """Dot product of two lists of equal length"""
    return sum(x_ * y_ for (x_, y_) in zip(x, y))


##############################################################################
# Solve these
##############################################################################
def transpose(X):
    """Transpose of a matrix `X`.

    Implement the transpose operator with only one line of code! More than one line of
    code do not qualify.

    See [1] for definition.

    Args:
        X: list of lists, with `len(X) == i` and `len(X[0]) == j` and i, j > 0.

    References:
        [1] https://en.wikipedia.org/wiki/Transpose

    """
    raise NotImplementedError


def matmul(X, Y):
    """Matric multiplication of two matrices `X` and `Y`.

    Implement the matrix multiplication operator with only one line of code!
    More than one line of code do not qualify.

    See [1] for definition.

    Notes:
        Use the `dot` helper function if you like. Maybe you also want to use
        some previously defined helper function, as well. :-)

    Args:
        X: list of lists, with `len(X) == I` and `len(X[0]) == J` and I, J > 0.
        Y: list of lists. with `len(Y) == J` and `len(X[0]) == k` and J, K > 0.

    References:
        [1] https://en.wikipedia.org/wiki/Matrix_multiplication
    """
    raise NotImplementedError

    assert len(X[0]) == len(Y), "Shape mismatch. Can't do matrix multiplication."


def submatrix(X, i, j):
    """Calculate the submatrix of `X` by removing row `i` and column `j`.

    See [1] for reference.

    Args;
        X: list of lists, with `len(X) == I` and `len(X[0]) == J` and I > 0

    Returns:
        Y: A list of lists, with `len(Y) == I-1` and `len(Y[0]) == J - 1`

    Example:
        >>> X = [[1, 2, 3],
        >>>      [4, 5, 6],
        >>>      [7, 8, 9]]
        >>> submatrix(X, 1, 1)
        [[1, 3],
         [7, 9]]

    References:
        [1] https://en.wikipedia.org/wiki/Minor_(linear_algebra)
    """

    raise NotImplementedError

    I, J = shape(X)
    assert I > 1 or J > 1, "Matrix too small to find submatrix"


def determinant(X) -> float:
    """Determinant of a matrix `X`.

    Determinant calculation must be done using Laplace expansion. See [1] for an
    example. For simplicity, you can just do Laplace expansion along the first row.

    The implementation should be foremost CORRECT and CLEAN. We don't care about
    performance. If we wanted performance, we would probably not implement matrix
    operations directly in Python, and we would certainly not use the Laplace expansion
    method. There's not much to do on the Moon anyways, so algorithm speed is no
    problem.

    Args:
        X: list of lists, with `len(X) == I` and `len(X[0]) == I` with I > 0

    Returns:
        The determinant of matrix `X` (a single float value).

    Notes:
        The matrix `X` is square! We cannot find the determinant of non-square matrices.

        Also, we expect that you will implement a recursive function here, because the
        Laplace transform has a more-or-less recursive definition.

    References:
        [1] https://en.wikipedia.org/wiki/Laplace_expansion
    """
    raise NotImplementedError

    # NOTE: You can use more than 1 line of code to implement this. :-)
