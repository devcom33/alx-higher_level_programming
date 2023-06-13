#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if not my_list:
        my_list.copy()
    if idx < 0:
        return my_list.copy()
    if len(my_list) <= idx:
        return my_list.copy()
    my_list[idx] = element
    return my_list
