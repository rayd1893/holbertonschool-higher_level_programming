#!/usr/bin/python3
'''Model Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
        '''Class Square'''

        def __init__(self, size, x=0, y=0, id=None):
                super().__init__(size, size, x, y, id)
                self.__size = size

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
