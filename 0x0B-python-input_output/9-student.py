#!/usr/bin/python3
'''Class student'''


class Student:
    '''Define class'''
    def __init__(self, first_name, last_name, age):
        '''Define constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Define dictionary'''
        return self.__dict__
