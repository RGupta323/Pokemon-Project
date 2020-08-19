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

    #test for pokemon moves
    def test_loadmovejson(self):
        #load all the json into ./Files/Moves/ from PokeAPI
        path = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Move\\"
        i=1
        while(i>0):
            try:
                print("Loading move json with id: {}".format(i))
                get_json(type='Move', i=i)
            except Exception as e:
                print("An error occured! Exception: {}".format(e))
                break
            i+=1 #this is unnecessary

    # adding moves in the ./Files/Move directory into the database
    def test_addmove(self):
        path = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Move\\"
        moves = os.listdir(path)


        for move in moves:
            move_dict = JSON.read(path+move)

            # assemble data dictionary
            data = dict()
            keys = {'damage_class':str, 'accuracy': int, 'id': int, 'power':int, 'name':str, 'pp':int,
            'type':str, 'effects': str}

            # define damage_class, accuracy, id
            data['damage_class'], data['accuracy'] = move_dict['damage_class']['name'], move_dict['accuracy']
            if(data['accuracy']==None):
                data['accuracy'] = 100
                
            # define id, power, name
            try:
                if(move_dict['power']==None or move_dict['power']=='None'):
                    data['id'], data['power'], data['name'] = int(move_dict['id']), 0, move_dict['name']
                else:
                    data['id'], data['power'], data['name'] = int(move_dict['id']), int(move_dict['power']), move_dict['name']
            except Exception as e:
                print("ERROR {} occured in line 97".format(e))
                print("Here's move_dict: " + str(move_dict))
                a = input("Would you like to alter the data? Type y or n: ")
                if(a=='y'):
                    id, power, name = input("id: "), input("power: "), input("name: ")
                    data['id'], data['power'], data['name'] = int(id), int(power), name

            # define type, pp
            try:
                data['type'], data['pp'] = move_dict['type']['name'], move_dict['pp']

            except Exception as e:
                print("ERROR {} occured on line 108!".format(e))
                a = input("Would you like to alter the data? Type y or n: ")
                if (a == 'y'):
                    type, pp = input("type: "), input("pp: ")
                    data['type'], data['pp'] = type, pp

            # define effects - making sure its in english
            try:
                data['effects'] = [effect['effect'] for effect in move_dict['effect_entries'] if(effect['language']['name']=='en')][0]

            except Exception as e:
                print("ERROR {} occured on line 122".format(e))
                a = input("Would you like to alter the data? Type y or n: ")
                if (a == 'y'):
                    effect = input("effect: ")
                    data['effects'] = [effect]

            # now add the newly data to the database
            print("Adding {} to the database".format(data))
            add_move(data)

        self.assertEqual(True, True)

    #test to load json locally
    def test_loaditemjson(self):
        # load all the json into ./Files/Moves/ from PokeAPI
        path = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\item\\"
        i = 1
        while (i > 0):
            try:
                print("Loading move json with id: {}".format(i))
                get_json(type='item', i=i)
            except Exception as e:
                print("An error occured! Exception: {}".format(e))
                break
            i += 1  #this is unnecessary

    #add item to data
    def test_additem(self):
        path = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\item\\"
        items = os.listdir(path)

        for item in items:
            item_dict = JSON.read(path+item)

            # assemble data dictionary
            data = dict()
            keys = {'id': int, 'name': str, 'effects': str
                    }

            #print("Adding {}".format(item_dict))

            # define id, name
            try:
                data['id'], data['name'] = int(item_dict['id']), item_dict['name']
            except Exception as e:
                print("ERROR {} occured in line 152 in test_additem() in DatabaseTest.py".format(e))
                print("Here's the item: {}".format(item_dict))

                a = input("Would you like to modify id and name (y/n): ")
                if(a == "y"):
                    id = input("id: ")
                    name = input("name: ")
                    data['id'], data['name'] = int(id), name

            # define effect
            try:
                data['effect'] = [effect['effect'] for effect in item_dict['effect_entries'] if(effect['language']['name'] == "en")][0]
            except Exception as e:
                print("Error {} occured on line 165".format(e))
                print("Here's the item: {}".format(item_dict))
                a = input("Would you like to modify the effect? (y/n): ")
                if(a == 'y'):
                    effect = input("effect: ")
                    data['effect'] = effect


            # call add_move()
            print("Adding {} to item table".format(data))
            add_item(data)


        self.assertEqual(True, True)

    def test_gettest(self):
        tables = ["item", "Move", "Pokemon"]
        for i in range(1,11):
            item = {'id':i}

            for table in tables:
                print(get(table, item))

        self.assertEqual(True, True)









if __name__ == '__main__':
    unittest.main()
