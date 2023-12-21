#!/usr/bin/python3
"""a function that prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        return int(''.join(map(str, my_list)))
    except Exception as e:
        print(e)
