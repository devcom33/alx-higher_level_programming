#!/usr/bin/python3
"""
    A function that adds 2 integers
"""
def add_integer(a, b=98):
    if type(a) is not int:
        raise "a must be an integer"
    if type(b) is not int:
        raise "b must be an integer"
    if type(a) is not float:
        raise "a must be an integer"
    if type(b) is not float:
        raise "b must be an integer"
    return a + b
