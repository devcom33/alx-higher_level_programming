#!/usr/bin/python3
"""
    A function that adds 2 integers
"""


def add_integer(a, b=98):

    """
        Add two integers

        Args:
            a: the first parameter
            b: the second parameter

        Raises:
            TypeError: if a, b arent int or float

        Returns:
            Sum of two int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/0-add_integer.txt")
