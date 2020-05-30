'''
this is a file that is going to contain functions to simulate a given website, and emulate it.
and scrape data from it, then format it so it can be used as an input to the csv functions.
'''
import requests
from bs4 import BeautifulSoup as bs
from Errors import *
from urllib.request import Request, urlopen

'''
Function parse() is going to search based on a url and a tag, adn going to return whatever it finds. 
This is going to be the main function so to speak, essentially it is going to determine 
whether if the user wants to spyder or what parameters the user wants to scrape a specific 
url and then is going to delegate it to one of its helper functions. 

To spyder means that its going to scraping a tags and then branching off of to those links 
Then that spyder function will return a list of urls to then call teh parse function on 
which the user will determine. 

The main inputs however are going to be a dictionary which essentialy will tell what everything is, 
so it will tell you what the tags, id, class_name are... 
And if something is nested the dictionary will look like this: {'tag':{'div':{'span':{'a'}}},'class_name':class, 
'id':whatever} 

Inputs: 
    url is a string that signifies the url that we are going to be webscraping 
    d is a dictionary that tells you what the tags, id and class_name are, those are the keys. 
    spyder is a boolean value that tells the function to look for a tags within the url and 
    return a list of those urls that are in the href tag. 

Logic: 
   Delegates which function to call based on parameters. 
    ..... 
Outputs: 
    a list of links if spyder is True
    a string if the data has been successfully parsed giving you the data. 
'''
def parse(url, d, spyder=False):
    #A little error check, if the url is none or the tag is an error raise an error
    if(url==None or d==None):
        raise CustomError("Url or input dictionary d cannot be None");
    #another error check, make sure that the tag value isn't None.
    try:
        tag,id,class_name=d['tag'],d['id'],d['class_name'];
    except Exception as e:
        print("line 46, parse()");
        raise CustomError("Error with input dictionary getting tag, id and class_name values.")

    #if spyder is true then you're looking for a tags in whatever configuration that you die.
    if(spyder):
        return spyder(url,d);
    else:
        #proceed normally
        return parse_normal(url,d);

#for dealing with teh nromal case...
'''
Function that gets the content needed to parse a url from the main parse() function. 

Inputs
    url is a string that specifies the url 
    d is a input dictionary, whose ksys are 'tag','id','class'
    
Logic
    It will call the gethtml() function to get a beautiful soup object based on the url
    Then it will process the dictionary's values for tags, id and class and will use it to then 
    return a string of all the conetnet. 
    
Outputs: 
    A string or a list which contains information on the text that is to be webscraped. 
'''
def parse_normal(url,d):
    soup=gethtml(url,d);
    #boolean variables..
    has_id,has_class=True,True;
    try:
        id=d['id']
    except Exception as e:
        has_id=False;
    try:
        class_name=d['class']
    except Exception as e:
        has_class=False;

    if(has_id):
        bs=soup.find(d['tag'],{'id':d['id']})
    if( has_class):
        bs=soup.find(d['tag'], class_=d['class'])
    if(has_id and has_class):
        bs=soup.find(d['tag'],id=d['id'], class_=d['class'])

    return ([element for element in bs])


#function to return a html content based on values on input dictionary
'''
Returns a beautiful soup object with html content as input based on a url and an input dictionary

Inputs: 
    url is a string that specifies the url of the site to be webscraped 
    d is a dictionary that contains the keys of tag, id and class_name in that order
        It specifies if  a tag is nested or not... 
        
Logic 
    Does an error check, if the tag value of the dictionary or the url or teh dictionary itself isn't 
    valid, then raise an error and return None. 
    Other than that return a beautiful soup object with a html content as input

Outputs: 
    a beautiful soup object with urlopen(url)
'''
def gethtml(url,d):
    try:
        tag=d['tag']
    except Exception as e:
        print("line 83, gethtml()")
        print(e);
        return None;
    #the tag can never be None. if it is return an error
    if(tag==None or url==None):
        print("line 52; gethtml() function")
        print("tag parameter can never be None");
        raise CustomError("Invalid Argument tag. Tag parameter can never be None")
        return None;
    return bs(urlopen(url),'html.parser')


#function spyder(), to return a list of urls
def spyder(url,d,nested=False):


#function to deal with nesting tags...
def nesting(url,d):
    pass;

#helper function to see if nesting is true or false, it will depend on the configuration of the dictionary
def isNested(d):
    try:
        isNested=type(d['tag'])==dict
    except Exception as e:
        print("line 91, isNested() function. ")
        raise CustomError("Error accessing value of 'tag' key in, input dictionary")
        return e;
    return isNested;

