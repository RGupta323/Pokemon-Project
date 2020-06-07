'''
This is a file with functions to read, write and append to a JSON file.
'''
from Errors.Errors import *;
'''
Function to read a JSON file. 
'''
def read(file):
    try:
        f=open(file,'r');
        r=f.read()
        f.close()
    except Exception as e:
        raise CustomError("Error has occured")
        return False;
    print(r);
    return True;
'''
Function to write to a JSON file. 
'''
def write(file, content):
    pass;

'''
Function to append to an existing JSON file. 
'''
def append(file,content):
    pass;

'''
Function to print all data from a given JSON file. 
'''
def print(file):
    pass;