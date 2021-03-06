'''
this is a file that is going to contain functions to simulate a given website, and emulate it.
and scrape data from it, then format it so it can be used as an input to the csv functions.
'''
import requests
from bs4 import BeautifulSoup as bs
from Errors.Errors import *
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
    #take care of nesting case...
    if(isNested(d)):
        return nesting(url,d);
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
'''
This function is going to, ideally, return the urls in the a tags that are in the href attribute. 
If something is nested, that gets trickier, first 'spyderify' the dictionary to make sure the last tag are a tags. 
So if it is nested, then you need to 'un-nest' these tags, show us what we're doing and then 
'''
def spyder(url,d):
    nested=isNested(d);
    if(nested):
        #So this is a tricky case here, spyder() needs to scrape a tags, and if it is nested
        #then you need to take care of the nesting tags as well...
        return nesting(url,d,spyder=True);
    html=gethtml(url,d);
    pass;

#function to deal with nesting tags...
'''
So this is dealing with the case that the tags are nested. It deals with that case using beautiful soup. 
So if your input dictionary looks something like this: 
d={'tag':{'div':{'span':'a'}}, 'class':{'div':'infocard'}, id=None} 
This tells us that you're looking for an a tag inside a span tag inside a div tag. 
Now the class tag tells us that all divs must have the class 'infocard'. 
Our final destination is to get those a tags. 

Kind of a preliminary case, you want to check if the spyder which is a boolean value if it is true or not. 
If you're going to spyder basically that means you wanna 'spyderify' the input dictionary d so to speak so call 
d=spyyder_dict(d), and then call the spyder() function. 

Inputs: 
    url is a string that specifies the url 
    d is a input dictionary, properly formatted. 
    spyder, an optinoal boolean variable, that tells you if it needs to be spydered so to speak. 
    
Logic: 
    So if spyder is true: 
        d=spyder_dict(d); 
        Which means you're going to be looking for a tags at the end 
        Then you wanna scrape all the a tags, whatever they're nested inside. 
        Call spyder()
    Else, 
        So start with the outter most tag, and get all teh content out of that with getHTML(), 
        then use bs within that object scrape all the tags within, so its going to be more of a infinite loop... 

Output
    Raise an error and return None, if there are any errors. 
    If not, return an iterable bs object ie namelist=bs.findAll('span'), return namelist; 
'''
def nesting(url,d,spyder=False):
    if(spyder):
        pass;

#helper function to see if nesting is true or false, it will depend on the configuration of the dictionary
def isNested(d):
    try:
        isNested=(type(d['tag'])==dict)
    except Exception as e:
        print("line 91, isNested() function. ")
        raise CustomError("Error accessing value of 'tag' key in, input dictionary")
        return e;
    return isNested;

#Another helper function to essentially spider-ify a dictionary
#when the spyder() function is called, and the input dict d is nested then you have to make sure
#that the last tag is an a tag...
def spyder_dict(d):
    #first search the input dictionary and see if there is an a tag as the last value of the tag key...
    #if there is return the dictioanry, if there isn't add it.
    if(getTag(d,key='tag',i=depth(d,key='tag'))=='a'):
        return d;
    temp=get_i_dict(d,key='tag',i=depth(d,key='tag'));
    k,v=list(temp.keys())[0],list(temp.values())[0]
    temp[k]={v:'a'}
    d['tag']=temp;
    return d;



#helper recursive functiosn here...

#depth() function, given a key and a dictionary to see how nested a dictionary is given a key.
def depth(d,key):
    if(type(d[key])!=dict):
        return 0
    d=d[key]
    k=list(d[key].keys())[0]
    return 1+depth(d,k)

#getTag() helper function,
#given a dictionary d, a key in d.keys(), and an integer i
#where i specifies inside the nested dictionary, waht ith value they want
def getTag(d,key,i):
    if(i==0):
        return d[key]
    d=d[key]
    k=list(d.keys())[0]
    return getTag(d,k,i-1)
#helper function to get an ith dictionary of a nested dict
def get_i_dict(d,key,i):
    if(i==0):
        return d;
    d=d[key]
    k=list(d.keys())[0]
    return get_i_dict(d,key,i-1)