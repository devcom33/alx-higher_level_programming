#!/usr/bin/python3
"""
    A function that adds 2 integers
"""


def add_integer(a, b=98):

    """
        Add two integers
        A function that takes two numbers, a and b returs sum

        Usage:
        >>> add_integer(4,7)
        11
        >>> add_integer(-2, 2)
        0
    """
    if type(a) is not int:
        raise "a must be an integer"
    if type(b) is not int:
        raise "b must be an integer"
    return a + b


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/0-add_integer.txt")
