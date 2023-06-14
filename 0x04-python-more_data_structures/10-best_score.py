#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    x = a_dictionary.values()
    return list(a_dictionary.keys())[list(a_dictionary.values()).index(max(x))]
