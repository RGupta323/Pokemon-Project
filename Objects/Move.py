#class to store a Pokemon's move
import os
#from Data.PokeAPI import get_json

class Move:
    def __init__(self,name,accuracy, damage_type, power, pp, type, effects):
        self.name=name
        #move attributes
        self.accuracy = accuracy
        self.damage_type = damage_type
        if(self.damage_type=="status"):
            self.power = None
        else:
            self.power = power
        self.pp = pp
        self.type = type
        self.effects = effects

