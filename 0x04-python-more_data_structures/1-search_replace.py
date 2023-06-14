#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            my_list[my_list.index(i)] = replace
    return my_list
