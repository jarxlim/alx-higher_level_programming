#!/usr/bin/python3
'''contains a rectangle class'''


class Rectangle:
    '''a class Rectangle that defines a rectangle by:'''

    def __init__(self, width=0, heigth=0):
        ''' instantiation of the rectangle class'''
        self.width = width
        self.heigth = heigth

    @property
    def width(self):
        '''retrieving the width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets the width atttribute'''
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise TypeError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def heigth(self):
        '''retrieving the heigth attribute'''
        return self.__heigth

    @heigth.setter
    def heigth(self, value):
        '''sets the heigth atttribute'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
