#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = {x for x in set_1 if x not in set_2}
    new_set.update(x for x in set_2 if x not in set_1)
    return new_set
