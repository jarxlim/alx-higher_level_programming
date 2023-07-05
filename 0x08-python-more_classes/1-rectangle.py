#!/usr/bin/python3
'''contains a rectangle class'''


class Rectangle:
    '''a class Rectangle that defines a rectangle by:'''

    def __init__(self, width=0, height=0):
        ''' instantiation of the rectangle class'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''retrieving the width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width atttribute'''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''retrieving the heigth attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets the heigth atttribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
