#!/usr/bin/python3
'''Defined Class Rectangle'''


class Rectangle:
    '''
    Class Rectangle
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Defined constructor'''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        '''Defined function str'''
        string = ""
        if self.__height == 0 or self.__width == 0:
            string = ""
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    string += str(self.print_symbol)
                string += "\n"
        return string[:-1]

    def __repr__(self):
        '''Defined function repr'''
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        '''Delete class'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        '''Getter width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculate area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate perimeter of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Method static - Compare two classes'''
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''Class method - Return new class'''
        return cls(size, size)
