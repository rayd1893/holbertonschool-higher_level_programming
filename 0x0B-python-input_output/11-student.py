#!/usr/bin/python3
'''Class student'''


class Student:
    '''Define class'''
    def __init__(self, first_name, last_name, age):
        '''Define constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Define dictionary'''
        new_dict = {}
        if type(attrs) is list:
            for key in attrs:
                try:
                    new_dict[key] = self.__dict__[key]
                except:
                    pass
        else:
            new_dict = self.__dict__
        return new_dict

    def reload_from_json(self, json):
        '''Define reload dictionary'''
        for (key, value) in json.items():
            self.__dict__[key] = value
