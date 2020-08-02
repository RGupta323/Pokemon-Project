import unittest

from Data.Database import *
import os
from Data import JSON
from Data.PokeAPI import get_json
class MyTestCase(unittest.TestCase):
    def test_tableexists(self):
        self.assertEqual(check_table(), True)

    def test_addpokemon(self):

        data = {"id": int, "name": str, "types": str, 'weight': int, 'height': int, 'hp': int, 'attack': int,
                    'speical-attack': int, 'defense': int,
                    'special-defense': int, 'speed': int, 'abilities': str
                    }

        # execute add_pokemon() function in Database.py
        pokemon = os.listdir("C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Pokemon\\")
        for p in pokemon:
            #open the json folder up, and load it into a dictionary
            poke_dict = JSON.read("C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Pokemon\\"+p)

            #assemble data dictionary for each pokemon
            d = dict()
            #id, name
            d['id'], d['name'] = int(poke_dict['id']), p.split(".")[0]

            #types
            d['types'] = " ".join([type['type']['name'] for type in poke_dict['types']])
            #weight, height
            d['weight'], d['height'] = int(poke_dict['weight']), int(poke_dict['height'])

            #stats: hp, attack, sp_atk, defense, sp_def, speed
            for stat in poke_dict['stats']:
                d[stat['stat']['name']] = int(stat['base_stat'])

            #abilities -> form a string (separated by spaces) with the abilities names
            d['abilities'] = " ".join([ability['ability']['name'] for ability in poke_dict['abilities']])

            #use database add function()
            add(d, "Pokemon")
        self.assertEqual(True, True)

    def test_addability(self):
        abilities = os.listdir("C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\ability\\")
        for ability in abilities:
            ability_dict = JSON.read("C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\ability\\"+ability)
            #format data dictionary as input to add_ability() 
            d = dict() 
            
            #name 
            d['name'] = ability_dict['name']
            
            #effect 
            d['effect'] = [effect['effect'] for effect in ability_dict['effect_entries'] if(effect['language']['name'] == 'en')][0]
            #execute add_ability() function in Database.py
            add_ability(d)
        
            
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
