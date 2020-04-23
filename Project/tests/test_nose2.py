#!python
# coding: utf-8

"""
Tests for Main.py
"""

import unittest
from nose2.tools.params import params
# other imports


class TestCase1(unittest.TestCase):
    """
    Small description of test case
    """

    def setUp(self):
        """initialize whatever is necessary to run all tests in this class"""

    def test_situation_1(self):
        self.assertFalse('function_to_test(args)')

    @params(-1, 0, 1, 999999)
    def test_situation_2(self, parameter):
        self.assertIsInstance(parameter, int)


class TestCase2(unittest.TestCase):
    """
    Small description of test case
    """
    def test_situation_3(self):
        self.assertEquals('function_to_test(args)', 'output')
