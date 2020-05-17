#this is going to be a file full of object classes that are going to be used for the database;
"""
There are 3 tables so there's gonna be a different entry each time.

Moves_entry, Stats_entry, Pokemon_entry; these will contain data to push into the database;
"""


"""
Pokemon_Entry(id,name,types,abilities,height,weight, gender,evolution)
id is an integer, signifying the id number of the pokemon
name is a string, the name of the pokemon 
types is a string separated by a comma indicating the type of the pokemon 
abilities is a string separated by comma indicating the name of the abilities that the pokemon has 
height is a integer, indicating the height of the pokemon (rounded up) in meters
weight is an integer, indiciating the weight of hte pokemon (rounded up) in kilograms
gender is a string, indicating male or female. 
evolution is a string indicating hte next evolution, for the pokemon 

Here's an example: 
bulbasaur = Pokemon_Entry(01,"bulbasaur","grass,poison","overgrow,cholorphyl",1, 7,"male","ivysaur")
"""
class Pokemon_Entry:
    def __init__(self, id, name, types, abilities, height, weight, gender, evolution):
        self.id=id;
        self.name=name;
        self.types=types;
        self.abilities=abilities;
        self.height=height;
        self.weight=weight;
        self.gender=gender ;
        self.evolution=evolution;
        self.data=[self.id,self.name,self.types,self.abilities,self.height,self.weight,self.gender,self.evolution]
        self.cols=["id","name","types","abilities","height","weight","gender","evolution"]
