#!/usr/bin/python3
import sys

def dyn_args():
    cnt = 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for k in sys.argv[1:]:
            print("{}: ".format(cnt, k))
            cnt += 1
if __name__ == "__main__":
    dyn_args()
