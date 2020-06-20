import unittest
from Data.PokeAPI import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_getpokemon(self):
        self.assertNotEqual(get_pokemon(1),False)

    #test function to get pokemon some more pokemon
    def test_getmultiplepokemon(self):
        for i in range(2,11):
            self.assertNotEqual(get_pokemon(i),False)


if __name__ == '__main__':
    unittest.main()
