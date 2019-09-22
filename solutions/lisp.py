#!/usr/bin/env python

"""
Difficulty: 2

You are a developer that really loves Lisp (the programming language). Using only
notepad you have implemented a huge expression to try to find the faults and horizons in
a dataset.  Given that you don't have a linter, you are not sure whether your
expression is valid. Therefore you decided to implement an algorithm to check if every
parenthesis has the appropriate closing bracket.
"""


def is_valid_lisp(expression: str) -> bool:
    """
    Args:
        expression: Your expression as a string. Will only contain lower case letters,
            spaces and parenthesis.

    Returns:
        Whether the expression is valid. You can assume it is valid if every
        parenthesis has the appropriate closing parenthesis.

    Example:
        >>> print(is_balanced("(("))
        False
        >>> print(is_balanced("(()))("))
        False
        >>> print(is_balanced("()"))
        True
        >>> print(is_balanced("(h(e)l(l)o)"))
        True
    """
    # Allowed parenthesis
    open_parenthesis = '('
    close_parenthesis = ')'

    # Mapping open parantheses to respective close ones
    map = dict(zip(open_parenthesis, close_parenthesis))

    # Queue containing current open parenthesis but not closed
    queue = []

    # Foreach char..
    for c in expression:

        # If is an open parenthesis, put in in queue
        if c is open_parantheses:
            queue.append(map[c])

        # if is a close parenthesis,
        # check if there's one open in the queue
        elif c in close_parantheses:
            if not queue or c != queue.pop():
                return False

    # If, at the end, I've no element in the queue,
    # it's all balanced
    if len(queue) == 0:
        return True

    else:
        return False


