import unittest

from Data.Database import *
class MyTestCase(unittest.TestCase):
    def test_tableexists(self):
        self.assertEqual(check_table(), True)

    def test_addpokemon(self):
        # Load up all the json of all the pokemon id's 01 - 721 (inclusive)
        pokemon_ids = range(1, 722)
        # Pick a pokemon by the json

        # Assemble data dictionary

        # execute add_pokemon() function in Database.py
        pass


if __name__ == '__main__':
    unittest.main()
