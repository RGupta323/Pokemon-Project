'''File to contain a tree data structure.
Each node in the tree can have multiple children.
This will be used to essentially to parse the json and put
each element in the json to get to whatever keys and values you are looking for.
The root will always be an empty node and then from there you would parse the json.

So the json is a dictionary composed of other dictionaries, lists and values. The lists can be lists of dictionaries or list of lists
or lists of values. The root would be null and each children would be the first element in that row so {element1, element2, ..., elementn}
Then essentially it would keep having children until it was successfully parsed. For example 'abilities" in .json files of pokemon are
is a list of dictionaries, which contain other abilities so that would be parsed over and over until single values remain that would be
a dictionary.
'''
from Objects.Node import *;
class PokemonTree:
    def __init__(self):
        self.root = Node(parent=None, children=list(), data=None);

    #functions to create and delete subtrees... (this is going to be used to parse entire sections of the pokemon json)
