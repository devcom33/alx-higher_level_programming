#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = list(map(lambda x, y: x * y, a_dictionary.values()))
    return new_dic
