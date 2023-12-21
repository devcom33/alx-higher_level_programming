#!/usr/bin/python3
"""a function that prints x elements of a list"""


def safe_print_list(my_list=[], x=0):
    try:
        print(int(''.join(map(str, my_list[:x]))), end='')
        print("")
    except:
        print(0)
    return list_size(my_list, x)

""" a function that counts"""


def list_size(my_list=[], x=0):
    c = 0
    for i in my_list:
        c = c + 1
    if x <= c:
        return x
    return c
