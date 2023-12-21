#!/usr/bin/python3
"""a function that prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        print(int(''.join(map(str, my_list[:x]))), end='')
        print("")
        return x
    except Exception as e:
        print(e)
