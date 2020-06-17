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
        #print("entered method")
        baseurl="C:\\Users\\gupta\\PycharmProjects\\PokemonProject"
        r=read(baseurl+'\\Files\\test.json')
        test=(r!=False) #this is how we'll test these things if a function doesn't return false, that means
        #it worked and so it'll return the content or whatever its returning.
        self.assertTrue(test);
        self.assertEqual(True, test)
        self.assertEqual(type(r), dict);
        #self.assertEqual(True, False)

        print(r)
    #add more json tests to test write() function.
    def test_write(self):
        baseurl = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject"
        r=read(baseurl+"\\Files\\test.json")
        test=(r!=False)
        self.assertEqual(test,True)
        self.assertEqual(type(r),dict)
        file=baseurl+"\\Files\\test-write.json"
        #so let keys=None in this case, and test that portion of the code.
        #this is just writing a plain dictionary to an empty file at this point.
        w=write(file,d=r,keys=None, replace=False)
        self.assertEqual(w!=False,True)

    def test_write2(self):
        #generate a random dictionary and replace it
        baseurl = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject"
        r = read(baseurl + "\\Files\\test.json")





if __name__ == '__main__':
    unittest.main()
