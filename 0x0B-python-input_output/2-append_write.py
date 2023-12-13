#!/usr/bin/python3
"""a function that append a string to a text file"""


def append_write(filename="", text=""):
    """append a string to a text file
        Args:
            filename: name of the file
            text: content of the file
        Returns:
            the number of char
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
