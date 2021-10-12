#!/usr/bin/python3


'''File to class MyList'''


class MyList(list):
    '''Class MyList inheret object list'''
    def __init__(self):
        '''Define Constructor'''
        self.__newList = []

    def print_sorted(self):
        '''Print list sorted'''
        self.__newList = self.copy()
        self.__newList.sort()
        print(self.__newList)
