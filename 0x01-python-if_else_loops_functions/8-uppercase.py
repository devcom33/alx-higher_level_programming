#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            chr(ord(i) - 32);
            print("{:c}".format(chr(ord(i) - 32)), end='')
        else:
            print("{:c}".format(chr(ord(i) - 32)), end='')
    print('')

