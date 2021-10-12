#!/usr/bin/python3
'''Define class Square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square inheret Rectangle'''
    def __init__(self, size):
        '''Define constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''Define str'''
        name = type(self).__name__
        return "[" + name + "] " + str(self.__size) + "/" + str(self.__size)
