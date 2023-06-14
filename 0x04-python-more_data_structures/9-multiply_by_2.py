#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for i in a_dictionary:
        new_dic.update({i: a_dictionary.get(i) * 2})
    return new_dic
