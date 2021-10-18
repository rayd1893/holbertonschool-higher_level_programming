#!/usr/bin/python3
'''File Test class Rectangle'''


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Class test of Rectangle'''

    def test_id(self):
        r1 = Rectangle(10, 2)
        id = r1.id
        self.assertEqual(id, 2)
