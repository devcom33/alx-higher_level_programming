#!/usr/bin/python3
def weight_average(my_list=[]):
    u = 0
    v = 0
    for i in my_list:
        u += i[0] * i[1]
        v += i[1]
    return u / v
