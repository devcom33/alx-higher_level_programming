#!/usr/bin/python3

def no_c(my_string):
    new_strings = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_strings += i
    return new_strings
