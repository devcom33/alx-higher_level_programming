#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(text)
    return len(text)
