#class to store a Pokemon's move
import os
from Data.PokeAPI import *
from Data.JSON import *
class Move:
    def __init__(self,name,url):
        self.name=name
        self.url=url
        self.json = self.getjson();
        #move attributes
        self.accuracy = self.json['accuracy']
        self.damage_type = self.json['damage_class']['name']
        if(self.damage_type=="status"):
            self.power = None
        else:
            self.power = self.json['power']
        self.pp = self.json['pp'];
        self.type = self.json['type']['name'];
        self.effects = self.json['effect_entries'];

    #function to get json file of the move created. (ie tackle.json)
    def getjson(self):
        path = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Moves"
        os.chdir(path);
        exists = lambda name: os.path.isfile(name + ".json")
        if(not exists(self.name)):
            get_json("move",self.name);
        return JSON.read(path+"\\"+self.name+".json")




    def toString(self):
        return "{},{}".format(self.name,self.url)