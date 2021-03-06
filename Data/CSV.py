import csv
"""This file contains functions for reading and writing in a csv file. 
I HAD WAY TOO MANY ISSUES WITH DATABASES, there was a huge issue that sql didn't like 
double quoted strings, and needed single quotes but it was just too much trouble to deal with. 
I'm just going to make multiple csv files and maybe have some sort of trigger function where 
changes to a csv file will trigger it to migrate to a database of some kind."""

#this function creates a csv files and returns the name of teh file as output
#name is a string telling you the name of the csv
#attr is a list of strings that are going to be the first row where data can be written
def createCSV(name,attr):
    name=name+".csv"
    with open(name,'w') as csvfile:
        fw=csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        fw.writerow(attr)
        csvfile.close();

#function to write a csv file

'''Very similar to the write functions in the Database.py, the write function will take in a 
list of dictionaries attrs, and will then write to that csv file, and it takes in a csv file name 

Inputs: 
    Attrs is a list of n dictionaries. Let d be each dictionary inside this list where d is a 
    dictionary formatted like this {column-name1:data, column-name2:data,....column-namen:data} 
        Ex. {id:1,name:'bulbasaur',types:'grass,poison',....} 
    fileName is a string that contains the name of the csv file. 

Logic: 
    Open the csv file
    Loop through Attrs and called the writerow() function on every d dictionary, writing their 
    values as a list. 

Output: 
    return True if completed; 
    If any errors, return False and print the error as well as the line number associated. 

 '''
def write(fileName, attrs):
    try:
        with open(fileName,"a",newline="") as file:
            #print("line 42, entered");
            fw=csv.writer(file,delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL);
            #its 1 to skip the first row;
            for i in range(0,len(attrs)):
                #print("line 46, entered loop")
                d=attrs[i];
                #print(d);
                #print(d.values())
                fw.writerow(d.values());
            file.close()
    except Exception as e:
        print("entered");
        print("line 46");
        print(e);
        return False
    return True;

#function to read a csv file
'''
There will be ONE function to read a csv file 
Essentially it will return a list of dictionaries where each dictionary d, its keys are 
the names of the columns and its values are the values of each row of those columns

Inputs: 
    fileName is a string of a csv that will be read 
    i is an optional argument that is between 1 and n for a csv n rows, by default i is set to -1, 
    this will indicate if a specific row needs to be called upon. 
    
Logic: 
    If i is -1:
        Then open the csv file, loop through each row in the csv.reader, 
        For each row (skipping the first row), construct a dictionary for each row and 
        append it to the list that you will return; 
    
    Else: 
        Then open the csv file, loop through each row in teh csv.reader, 
        Find the row that matches i, and construct a dictionary for that row, and return it in 
        a list format. 

Outputs: 
    reutrn a list of dictionaries; 
    Also return False, if there are any errors that occur. 
'''
def read(fileName, i=-1):
    try:
        lis=list()
        f=open(fileName,"r")
        reader=csv.reader(f);
        first=True;
        #print(len([row for row in reader]))
        for row in reader:
            if(i==0):
                #assemble dict
                return read_helper(fileName, row)
            if(first):
                first=False;
                continue;
            #ASSEMBLE DICTIONARY
            lis.append(read_helper(fileName, row))
        f.close()
        return lis
    except Exception as e:
        print("line 96");
        print(e)
        return False;

#helper function, read_helper()
'''
Input: Takes in a list generated by csv, called a
    FileName is a string indicating the csv file 
    a is a list generated by the csv read() function
Logic: 
    Call upon read(fileName,0) which will give you the keys of the dictionary. 
    Then the values of the dictionary to be returned are the elements in the list 
    Helpful hint: the keys and values are teh same length so this can be done in one loop 
Output: 
    the dictionary created 
Why? 
    This will help the read() function, create a list of dictionaries 
'''
def read_helper(fileName,a):
    d=dict()
    keys=getRow(fileName,0);
    #print(keys)
    for i in range(len(a)):
        try:
            k,v=keys[i],a[i]
            d[k]=v;
        except Exception as e:
            print("line 130")
            print(k);
            print(v);
            print(e)


    return d;
#another helper function designed to get the ith row of a csv
def getRow(fileName,i):
    f=open(fileName,"r");
    reader=csv.reader(f);
    j=0;
    a=None;
    for row in reader:
        if(j==i):
            a=row;
            break;
        else:
            j+=1
    f.close()
    return a;
def printCSV(fileName):
    #print(type(fileName))
    f=open(fileName,"r")
    #print(f)
    reader=csv.reader(f);
    for row in reader:
        print(row);
    f.close();



#checkCSV() function, checks the given csv file and corrects any new line enteries...
'''
    Function to check the csv function, and check if there are any new line entries and correct them... 
    
    Inputs: 
        fileName is a string that indicates a csv file to open 
        
    Logic: 
        Open the csv file
        Loop through the rows and return true if there are new line characters and correct them, OR
        if there are no new line characters (these new line characters come in the form of empty lists)
        return false if any errors. 
        Now once you know there are any empty lists, what you need to do is delete them, 
        you either have to re-write teh file and all of its data... 
'''
def checkCSV(fileName):
    f=open(fileName,"r");
    #create csv writer
    reader=csv.reader(f);
    #now loop through it...
    emptyLines=False;
    try:
        for row in reader:
            if(row==[]):
                #print(row);
                emptyLines= True;
                #now call a helper function to correct these rows.
                correctCSV(fileName);
    except Exception as e:
        print("line 192")
        print(e);
        return False;
    f.close()
    return emptyLines;

#helper function to re-write csv file to make sure tehre are no empty lines.
def correctCSV(fileName):
    #open the file, for reading.
    f=open(fileName,"r");
    #assemble a writer
    reader=csv.reader(f);
    #now get all the rows that aren't empty lists; this will be a list of lists.
    rows=[row for row in reader if(row!=[])]
    f.close()
    #now open the file for writing...
    f=open(fileName,"w",newline="")
    writer=csv.writer(f);
    #now write that entire csv file, adn write all the non-empty rows.
    for row in rows:
        writer.writerow(row);
    f.close()

