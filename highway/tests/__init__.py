"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import grequests

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ConcurrencyTest(TestCase):
    def setup():
        self.urls = [
            'http://localhost:8000/?highway={route}'.format(route='helveticode.com') for i in range(1000)
        ]

    def test(self):
        rs = (grequests.get(u) for u in urls)
        grequests.map(rs)
        

# def my_func(a_list, idx):
#     """
#     >>> a = ['larry', 'curly', 'moe']
#     >>> my_func(a, 0)
#     'larry'
#     >>> my_func(a, 1)
#     'curly'
#     """
#     return a_list[idx]

# def add_two(num):
#     "Return the result of adding two to the provided number."
#     return num + 2