#!/usr/bin/python3
"""Define a Magicclass matching a bytecode already exist by ALX"""


import math


class Magicclass:
    """Represent a Circle"""

    def __init__(self, radius=0):
        """Initialize a Magicclass
        Arguments:
            Radius (float or int): The radius of the new magicclass.
            """
        self.__radius = radius

    def area(self):
        """Return the area of the magicclass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the magicclass"""
        return (2 * math.pi * self.__radius)
