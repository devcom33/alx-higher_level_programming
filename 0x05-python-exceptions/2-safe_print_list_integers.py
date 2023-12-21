#!/usr/bin/python3
"""a function that prints the first x elements of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):

    c = 0
    for i in range(x):
        try:
            if str(int(my_list[i])) == str(my_list[i]):
                print("{:d}".format(my_list[i]), end="")
                c += 1
        except(IndexError, TypeError, ValueError):
            break
    print("")
    return c
