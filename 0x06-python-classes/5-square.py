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
    @property
    def size(self):
        """getter
        Returns:
            the size of a Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size of a square
        Args:
            value (int): value of square
        Raises:
            TypeError: if isnt int
            ValueError: if size <= 0
        Returns: None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of the Square
        Returns: Area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('*', end='')
