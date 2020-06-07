import unittest
from Data.JSON import *;
'''
File to test the functions from JSON.py. 
All test functions have to have test_ at the front of 
their function name, other wise those functions 
will not run. 
'''

class MyTestCase(unittest.TestCase):
    #dummy test case
    def test_something(self):
        #self.assertEqual(True, True)
        self.assertEqual(True, True);

    def test_readTest(self):
        print("entered method")
        baseurl="C:\\Users\\gupta\\PycharmProjects\\PokemonProject"
        r=read(baseurl+'\\Files\\test.json')
        self.assertTrue(r);
        self.assertEqual(True, r)
        #self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
