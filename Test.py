import unittest
from Database import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def add_test(self):
        e=Pokemon_Entry(id=1,name="test",types="test",abilities="test",height=-1,weight=-1,
                        gender="test",evolution="test")
        self.assertEqual(True, add(e,"Pokemon"))

if __name__ == '__main__':
    #unittest.main()
    MyTestCase(unittest).add_test();
