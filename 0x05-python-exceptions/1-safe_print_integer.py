#!/usr/bin/python3
"""a function that prints an integer with "{:d}".format()"""


def safe_print_integer(value):
    try:
        if str(int(value)) == str(value):
            print("{:d}".format(value))
    except ExceptionType:
        return False
    else:
        return True
