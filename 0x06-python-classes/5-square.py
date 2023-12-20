#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Constructors

        arguments:
            size: length of a side of a square
        """
        self.__size = size

    @property
    def size(self):
        """Property for the length of a side of this square

        Raises:
            TypeError: If is not an integer
            ValueError: If is negative
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of this square
        Returns:
            The size squared
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'"""
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="\n" if j is self.__size - 1 and i != j else "")
        print()
