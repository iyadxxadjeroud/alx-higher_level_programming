#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructors
        
        arguments:
            size: length of a side of a square
        Raises:
            TypeError: If is not an integer
            ValueError: If is negative
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        def area(self):
            """Area of this square
            Returns:
                The size squared
            """
            return self.__size ** 2
