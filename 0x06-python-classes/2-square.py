#!/usr/bin/python3
"""Define A Square Class"""


class Square:
    """A Square Class"""
    def __init__(self, size=0):
        """init a square
        Args:
            size (int): size of square
        Raises:
            TypeError: if isnt int
            ValueError: if size <= 0
        Returns: None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
