#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    if len(sys.argv) == 1:
        pass
    else:
        for k in sys.argv[1:]:
            s += int(k)
    print(s)
