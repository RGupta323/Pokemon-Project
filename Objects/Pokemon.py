'''Script to contain the PokemonObject()
Essentially it takes a JSON file of the pokemon's name, and has functions to get its types, abilities, moveset, types, etc.
The JSON file is parsed and separated upon creating that object.
'''
from Data.JSON import read
from Objects.Move import Move
from Objects.Ability import Ability
# from Objects.MegaPokemon import *
import json
class Pokemon():
    '''Takes in only one argument, which is going to be a json file in the format of pokemonname.json. It will parse the json and sort
    them out.
    Optional argument: moveset. If the user wants to provide a moveset, other than that we will assume the moveset is None.
    '''
    def __init__(self, jsonName:str, moveset=None):
        self.json = json.loads(jsonName); #file to be parsed
        if(moveset==None):
            self.moves = self.getMoves(moves=self.json['moves']) #a generateor object, to generate all the moves the pokemon has.
        else:
            self.moves=moveset
        self.abilities = self.getAbilities(abilities=self.json['abilities']) #an  list containing ability objects
        self.types=self.getTypes(self.json['types'])() #list of strings containing the types of the pokemon
        self.name= self.json['name'] #string containing the pokemon name
        self.weight, self.height = self.json['weight'], self.json['height'] #integers containing the weight and height of the pokemon respectively
        self.stats = self.getStats(stats=self.json['stats'])
        self.mega = self.findMega();


    #function to get the moves from a json dictionary
    #Returns a generator object to generate all moves that the pokemon has.
    def getMoves(self, moves:list):
        m = lambda move: Move(name=move['name'], url=move['url'])
        for move in moves:
            yield m(move['move'])

    #function to get abilities from json
    def getAbilities(self, abilities):
        return [Ability(a['ability']['name'], a['ability']['url']) for a in abilities]

    #function to get types
    #argument is a list of dictionaries directly from self.json['types']
    #parse it and figure just get the type names from it.
    def getTypes(self, types):
        return lambda : [d['type']['name'] for d in types]



    #function to get stats of a pokemon
    def getStats(self, stats):
        a = lambda stat: stat['base_stat']
        return {stat['stat']['name']: a(stat) for stat in stats}


    mega_pokemon = ["Venusaur", "Charizard", "Blastoise", "Alakazam", "Gengar",
                        "Kangaskhan", "Pinsir", "Gyarados", "Aerodactyl",
                        "Mewtwo", "Ampharos", "Scizor", "Heracross", "Houndoom",
                        "Tyranitar", "Blaziken", "Gardevoir,", "Mawile", "Aggron",
                        "Medicham", "Manectric", "Banette", "Absol",
                        "Garchomp", "Lucario", "Abomasnow", "Beedrill",
                        "Pidgeot", "Slowbro", "Steelix", "Sceptile", "Swampert",
                        "Sableye", "Sharpedo", "Camerupt", "Altaria", "Glalie",
                        "Salamence", "Metagross", "Latias", "Latios", "Rayquaza",
                        "Lopunny", "Gallade", "Audino", "Diancie"]




