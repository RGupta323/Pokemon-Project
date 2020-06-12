'''
This is a file with functions to read, write and append to a JSON file.
'''
from Errors.Errors import *;
import json
'''
Function to read a JSON file. 
Essentially this will return all the content, calls the .read() method. 

Inputs: 
    file which is a string that specifies an absolute path of a json file that is going to be read. 

Logic: 
    Open the file, read it, close the file and return the contents. 
    It'll catch any exceptions and raise an error if that occurs and print the exception that occurs. 
    
Output: 
    Will either return false or a dictionary that is parsed using the json library containing the file's contents. 
'''
def read(file):
    try:
        f=open(file,'r');
        r=f.read()
        if(r==""):
            raise CustomError("Line 13, r is empty")
            return False;
        f.close()
    except Exception as e:
        print(e)
        raise CustomError("Error has occured. read(file) function in JSON.py")
        return False;
    #print(r);
    return json.loads(r);


'''
Function to write to a JSON file. 
So this is a tricky one to write, because it really depends what you're going to be writing. 
so a JSON file is basically one gigantic dictionary of dictionaries. 
Every element so to speak is either another dictionary, a list of dictionaries or a value, so it can get 
pretty tricky to know which one you want to insert in. 

Inputs: 
    file is a string that specifies the absolute path of the json file
    d is a dictionary that will be written as a json string to the file. 
    d can also be a value. 
    keys is an optional argument that is either None or a list of strings 
    that specifies where the d should be inputed or where it should be 
    added. 
    replace is a optional boolean input, signifies if you want to replace a value in 
    the dictionary. 
    
Logic: 
    The first thing you need to figure out is where to input it. 
        Check if keys is None, if it is convert d into a json string 
        and write it into the file like normal. 
        If the keys aren't none, then in keys is a list of values, 
        if its nested thats a whole another story, so probably a good 
        idea to get some helper functions to figure out to get that 
        dictionary. 
        But an example is something like this, for test.json, 
        keys=['menu','popup'], and then d would be a dictionary to append
        or keys=['menu','popup','menuitem' if they want to append a dict 
        to a list of dictionaries. But if d is a value that s where you'd
        add that as well. 
        
    Once you input the dictionary, then return True, return False if 
    any errors occur. 
    

Outputs: 
    True if the run was successful. 
    False if it wasn't, print the error and raise a custom error. 
'''
def write(file, d, keys=None, replace=False):
    #open the file
    f=open(file,'w');
    if(keys==None):
        try:
            y=json.dumps(d);
            f.write(y);
            f.close();
            return True;
        except Exception as e:
            print(e);
            print("JSON.py, write(file,d,keys=None), lines 78-81")
            raise CustomError("Error. ")
    #if keys isn't none then call helper function to get the dict you want

    #modify the dict
    d=modify_dict(read(file),keys,content=d,replace=replace)
    #then write it into a file as a json string
    f.close()

'''
Function to print all data from a given JSON file. 
'''
def printJSON(file):
    r=read(file);
    if(type(r)==dict):
        print(r);
    return False;

#parsing dictionary functions
def modify_dict(d,keys,content,replace=False):
    try:
        element=get_dict(keys,d)
    except Exception as e:
        #print("line 110")
        print(CustomError("JSON.py, error with get_dict(keys,d) call, line 110"));
        return False;
    #so content in this case is either going to be a value or another dict to add to a
    # list of dictionaries or another dictionary itself.
    if(type(d)!=dict or replace):
        #now treat it as a value
        try:
            k=get_dict_key(keys,d);
            element[k]=content
        except Exception as e:
            print(CustomError("JSON.py, modify_dict() function, line 118-119"))
            print(e);
            return False;
    else:
        #this will be the case to append a dictionary
        try:
            k=get_dict_key(keys,d)
            element[k].append(content)
        except Exception as e:
            print(CustomError("JSON.py, modify_dict(), lines 127-128"))
            print(e);
            return False;

    return element;

#this will take a dictionary and a list of keys that is in d and recursively
#navigate inside them and get the dict inside them.
#But this only works if nested...
def get_dict(keys,d):
    if(len(keys)==1):
        return d[keys.pop(0)]
    k=keys.pop(0)
    return get_dict(keys,d[k]);

def get_dict_key(keys,d):
    if(len(keys)==1):
        return keys[0]
    k=keys.pop(0)
    return get_dict_key(keys,d[k])
