__author__ = 'mranjan'


import unittest
import test2

class Testtest2(unittest.TestCase):
    def test_add(self):
        result=test2.add(10,3)
        self.assertEqual(result,13)