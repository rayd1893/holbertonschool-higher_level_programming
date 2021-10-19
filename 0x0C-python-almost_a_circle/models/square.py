#!/usr/bin/python3
'''Model Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
        '''Class Square'''

        def __init__(self, size, x=0, y=0, id=None):
                self.size = size
                super().__init__(size, size, x, y, id)

        def __str__(self):
                '''Define function str'''
                x = self.x
                y = self.y
                size = self.__size
                form = type(self).__name__
                txt = "[" + form + "] "
                txt += "(" + str(self.id) + ") "
                txt += str(x) + "/" + str(y) + " - "
                txt += str(size)
                return txt

        @property
        def size(self):
                '''Get size'''
                return self.__size

        @size.setter
        def size(self, size):
                '''Set size'''
                self.validator_integer("width", size, 1)
                self.__size = size
