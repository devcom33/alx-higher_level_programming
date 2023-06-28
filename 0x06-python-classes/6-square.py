#!/usr/bin/python3
"""Define A Square Class"""


class Square:
    """A Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """init a square
        Args:
            size (int): size of square
            positin (tuple): pos of sq
        Returns: None
        """
        self.size = size
        self.position = position

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
        """print square
        """
        if self.__size == 0:
            print('')
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print('#', end='')
                print()

    @property
    def position(self):
        """getter of the pos"""
        return self.__position

    @position.setter
    def position(self, value):
        """position of the square
            Args:
                value: value of the pos
            Raises:
                TypeError: position must be a tuple of 2 positive integers
        """
        if type(value) is tuple and len(value) == 2 and type(value[0]) == int and type(value[1]) == int and \
                value[1] >= 0 and value[0] >= 0:
                    self.__value = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        """getter of the pos"""
        return self.__position
