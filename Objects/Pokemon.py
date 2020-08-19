'''Script to contain the PokemonObject()
Essentially it takes a JSON file of the pokemon's name, and has functions to get its types, abilities, moveset, types, etc.
The JSON file is parsed and separated upon creating that object.
'''
from Data.JSON import read
from Objects.Move import Move
from Objects.Ability import Ability
# from Objects.MegaPokemon import *
import json
class Pokemon:
    '''Takes in only one argument, which is going to be a json file in the format of pokemonname.json. It will parse the json and sort
    them out.
    Optional argument: moveset. If the user wants to provide a moveset, other than that we will assume the moveset is None.
    '''
    def __init__(self, data, moveset=None):
        pass










