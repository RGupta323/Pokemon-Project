'''
This is going to be a file that is going to contain helper functions for my junit tests.
'''
#function to generate a random dictionary of strings
from random import random
from Errors.Errors import *;


def generatedict(length=-1):
    try:
        d=dict()
        if(length==-1):
            length=random.randint(1,10)
        for i in range(length):
            element_length=random.randint(1,5);
            k,v=generateStr(length=element_length)
            d[k]=v;
        return d

    except Exception as e:
        print(CustomError("Test.py generatedict() function, lines 10-19"))
        print(e);
        return False;

def generateStr(length=-1):
    try:
        if(length==-1):
            length=random.randint(1,5);
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        alpha += alpha.upper();
        return (''.join([alpha[i] for i in range(length)]))
    except Exception as e:
        print(CustomError("Test.py generateStr() function, lines 26-30"))
        print(e);
        return False;

#function to generate a random nested dictionary



