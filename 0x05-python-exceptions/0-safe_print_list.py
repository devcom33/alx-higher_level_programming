#!/bin/usr/python3
"""a function that prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list:
            print("{:d}".format(i), end="")
        print("")
    except Exception as e:
        print(e)
