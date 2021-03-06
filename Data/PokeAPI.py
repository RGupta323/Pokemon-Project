'''
This is a python script that has functions to gather data from the pokeapi about pokemon, moves, and
abilities and convert that info to json files and store them in the proper directory which will
be used for the actual ML portion of the project.
'''
import requests
import json
import os

from Objects.Pokemon import *
from Data import JSON

'''
This function uses PokeAPI (https://pokeapi.co/) and PokeBase (https://github.com/PokeAPI/pokebase)
to get information in a json file about a specific pokemon. 

Inputs(params): 
    i is an integer, where 1<=i<=649, it indicates the pokemon's id number to be called from 
    PokeAPI 

Logic: 
    make a request to the api using https://pokeapi.co/api/v2/pokemon/i 
    if the status code isn't 200, then print the error and break the function. 
    Take the json, and store it in an appropriate folder 
    
Outputs: 
    False if there are any errors
    Otherwise returns the json content as a python dictionary 
'''
#i can be a name or a number
def get_pokemon(i):
    try:
        response=requests.get("https://pokeapi.co/api/v2/pokemon/"+str(i))
        if(response.status_code!=200):
            print("status code: "+str(response.status_code))
            raise Exception("Status code not 200. PokeAPI.py, get_pokemon() function, line 26")
        #assuming the type of response is now json, write that into a file and store it
        #get the name of the json file
        response_dict=response.json()
        file_name=response_dict['name']

        #using the write() function in JSON.py to convert response to a dictionary then to a json string
        #and writing that as a json file and storing it in ...\\Files\\Pokemon\\file_name.json
        JSON.write(file="C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Pokemon\\"+file_name+".json",
                   d=json.dumps(response_dict))

        return response_dict
    except Exception as e:
        print("PokeAPI.py, get_pokemon() function, lines 30-42")
        print(e)
        return False

#this is a function that will return a Pokemon Object based on the input
def get_pokemon_obj(name:str, moveset=None):
    #check if name.json is in the Pokemon folder
    path = "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Pokemon"
    os.chdir(path);
    exists = lambda name : os.path.isfile(name+".json")
    if(not exists(name)):
        get_pokemon(name)
    #now return the Pokemon Obbject based on the name
    return Pokemon(jsonName=name+".json", moveset=moveset)

#function to get a json (either of a move, ability, pokemon or a number)
#type -> specifies a string indicating, move, ability, pokemon
#i -> an int or a string that specifies the id or name of the move or pokemon or ability (optional)

def get_json(type, i):
    try:
        response=requests.get("https://pokeapi.co/api/v2/{}/{}".format(type.lower(),i))
        if(response.status_code!=200):
            print("status code: "+str(response.status_code))
            raise Exception("Status code not 200. PokeAPI.py, get_pokemon() function, line 26")
        #assuming the type of response is now json, write that into a file and store it
        #get the name of the json file
        response_dict=response.json()
        file_name=response_dict['name']

        #using the write() function in JSON.py to convert response to a dictionary then to a json string
        #and writing that as a json file and storing it in ...\\Files\\Pokemon\\file_name.json
        JSON.write(file="C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\{}\\{}.json".format(
            type, file_name),
                   d=json.dumps(response_dict))

        return response_dict
    except Exception as e:
        print("PokeAPI.py, get_pokemon() function, lines 30-42")
        print(e)
        return False


#function to get a move json given a name
#i can be a name or the move id number
def get_move_json(i):
    try:
        response=requests.get("https://pokeapi.co/api/v2/move/"+str(i))
        if(response.status_code!=200):
            print("status code: "+str(response.status_code))
            raise Exception("Status code not 200. PokeAPI.py, get_pokemon() function, line 26")
        #assuming the type of response is now json, write that into a file and store it
        #get the name of the json file
        response_dict=response.json()
        file_name=response_dict['name']

        #using the write() function in JSON.py to convert response to a dictionary then to a json string
        #and writing that as a json file and storing it in ...\\Files\\Pokemon\\file_name.json
        JSON.write(file="C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Files\\Pokemon\\"+file_name+".json",
                   d=json.dumps(response_dict))

        return response_dict
    except Exception as e:
        print("PokeAPI.py, get_pokemon() function, lines 30-42")
        print(e)
        return False
