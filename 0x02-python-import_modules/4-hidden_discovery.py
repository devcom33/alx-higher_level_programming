#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4, sys
    lists = dir(hidden_4)
    for k in lists:
        if k[0] != '_':
            print(k)
