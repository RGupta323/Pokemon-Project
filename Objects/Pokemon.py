'''Script to contain the PokemonObject()
Essentially it takes a JSON file of the pokemon's name, and has functions to get its types, abilities, moveset, types, etc.
The JSON file is parsed and separated upon creating that object.
'''
from Data.JSON import read
class Pokemon():
    '''Takes in only one argument, which is going to be a json file in the format of pokemonname.json. It will parse the json and sort
    them out.
    Optional argument: moveset. If the user wants to provide a moveset, other than that we will assume the moveset is None.
    '''
    def __init__(self, jsonName, moveset=None):
        self.json = read(jsonName); #file to be parsed
        self.moves = None #a generateor object, to generate all the moves the pokemon has.
        self.abilities =[] #an  list containing ability objects
        self.types=[] #list of strings containing the types of the pokemon
        self.name= jsonName.split(".")[0] #string containing the pokemon name
        self.weight, self.height = -1 #integers containing the weight and height of the pokemon respectively
        self.stats = None #to be defined data structure to store teh pokemon's stats.


    #function to get the moves from a json dictionary
    #Returns a generator object to generate all moves that the pokemon has.
    def getMoves(self, moveset):
        #check if moveset is given (when moveset = None) if it is return it.
        if(moveset==None):
            return moveset

        #then create generator of all moves

    #function to get abilities from json
    def getAbilities(self):
        pass

    #function to get types
    def getTypes(self):
        pass

    #funciton to get weight
    def getWeight(self):
        pass

    #function to get height
    def getHeight(self):
        pass

    #function to get stats of a pokemon
    def getStats(self):
        pass