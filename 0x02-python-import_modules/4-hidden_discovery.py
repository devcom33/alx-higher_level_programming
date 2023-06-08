#!/usr/bin/python3
import hidden_4, sys
if __name__ == "__main__":
    lists = dir(hidden_4)
    for k in lists:
        if k[0] != '_':
            print(k)
