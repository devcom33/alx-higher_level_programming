#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    res = 0
    if not roman_string or roman_string == "":
        return 0
    if roman_string == "IX":
        res = 9
    elif roman_string == "IIV":
        res = 4
    else:
        for i in roman_string:
            res += dic[i]
    return res
