#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def dyn_args():
        cnt = 1
        if len(sys.argv) == 1:
            print("{} arguments.".format(0))
        elif len(sys.argv) == 2:
            print("{} argument:".format(len(sys.argv) - 1))
            print("{}: {}".format(1, sys.argv[1]))
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
            for k in sys.argv[1:]:
                print("{}: {}".format(cnt, k))
                cnt += 1
    dyn_args()
