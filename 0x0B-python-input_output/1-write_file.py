#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    with open(filename, 'a', encoding="utf-8"):
        filename.write(text)
