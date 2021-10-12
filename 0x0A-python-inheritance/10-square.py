#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''Define class Square'''


class Square(Rectangle):
    '''Class Square inheret Rectangle'''
    def __init__(self, size):
        '''Define constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
