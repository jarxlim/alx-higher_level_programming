#!/usr/bin/python3
"""Documentation for Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x coordinate attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y coordinate attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Displays/prints the Rectangle instance with a character #"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """str representation of the Rectangle instance"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the attributes in a list *args or **kwargs"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns a dictionary representation of a Rectangle instance"""
        newdict = {}
        newdict["id"] = self.id
        newdict["width"] = self.width
        newdict["height"] = self.height
        newdict["x"] = self.x
        newdict["y"] = self.y
        return newdict
