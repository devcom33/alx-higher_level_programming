#!/usr/bin/python3

for i in range(1, 89):
    if  int(str(i)[::-1]) >= i:
        if i > 9:
            if int(str(i)[::-1]) != i:
                print("{:02d}, ".format(i), end="")
        else:
            print("{:02d}, ".format(i), end="")
print("{:d}".format(89))
