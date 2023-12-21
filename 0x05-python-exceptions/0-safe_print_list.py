#!/usr/bin/python3
"""a function that prints x elements of a list"""

def list_size(my_list=[]):
    c = 0
    for i in my_list:
        c = c + 1
    return c

def safe_print_list(my_list=[], x=0):
    try:
        print(int(''.join(map(str, my_list[:x]))), end='')
        print("")
    except:
        print(x)
    return list_size(my_list)
