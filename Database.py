#Python file for all database functions
from databases import Database;
import mysql.connector;
import psycopg2;
from Entry import *
"""
So for this project we're going to be using PostgreSQL as a database; its a great back end database and its good to get
some experience with that.

So the database is going to have to multiple tables, with data filled with pokemon. For example, bulbasaur,
it has the id number of 001, and the first table is going to be labeled pokemon. So bulasaur will be registered as
<001,Bulbasaur,[Grass,Poison],ivysaur> so basically each entry in the table pokemon will be <id,name,types,evolutions>

Then with that id, it will go into another table called "moves" and its going to have that id along with all the moves
the pokemon can learn has learned.

Another table is created called "stats" which keyed by the id number of the pokemon will contain information about the
pokemon's stats based on the level (this can be determiend by you, as this is a little shakey).

So the other issue is how do you know what moves a pokemon knows? That will be handeld in a 
separate file, dedicated to webscraping pokemon info and formatting that data, then that 
data will be added to the database using these functions. d
"""
#connect(), returns a list of objects needed to facilitate database operations
#This works!
"""
This function connects to the database and returns an exception if there's an error
Returns a cursor object to execute other database commands. 
"""
tables=[]
def connect():
    try:
        user = "postgres"
        password = "Tofu1234"
        host = "localhost"
        port = "5432"

        conn=psycopg2.connect(database="Pokemon", user="postgres", password="Tofu1234")
        cursor=conn
    except Exception as e:
        print(e);
        return None;
    #cursor.close();
    #print("connection successful")
    return cursor;

#function that takes in a list of table names and creates those tables within the
#database
def check_tables():
    conn=connect();
    if(conn==None):
        print("line 56, ERROR")
        conn.close();
        return None;
    else:
        cur=conn.cursor()
        cur.execute(""" DROP TABLE Pokemon """)
        #cur.execute("""""")
        cur.close();
        conn.close();
#basic function of databases

#create table
#Where d is a list, which are the attributes or the columns of the table
#they're all type strings, so it creates a table
def create_table(table_name, d):
    conn=connect();
    cursor=conn.cursor()
    try:
        a=" varchar(255), ".join([str(k) for k in d])
        a+=" varchar(255)"
    except Exception as e:
        print("line 72");
        print(e);
        return False;
    #print(a);
    try:
        cursor.execute("""CREATE TABLE """+str(table_name)+"""( """+a+""");""")
        tables.append(table_name); #add table_name to tables;
    except Exception as e:
        print("line 75")
        print(e);
        return False;
    #cursor.commit();
    #print(cursor.fetchall());
    cursor.close();
    conn.commit();
    conn.close();


#add an entry from the database from a specific table t
#in this case, d represents a dictionary which stores an entry to be put into a table t
#first key, named "table-name" will have a string indicating the table name,
#the rest of the keys are the attributes of the table;
def add(d):
    if(d["table-name"].lower()=="pokemon"):
        add_pokemon(d)
    #other if statements here for other tables...
def add_pokemon(d):
    #create connection objects and cursor object
    conn=connect();
    cursor=conn.cursor();

    #formulate the command
    keys,values=[k for k in d.keys() if(k!="table-name")],[d[k] for k in d.keys() if(k!="table-name")]
    #command="""INSERT INTO {} ({}) VALUES ({});""".format(d["table-name"],add_helper(keys),
                                                         #add_helper(values));
    #print(len(values))
    print(values)
    command="INSERT INTO POKEMON VALUES(%s,%s,%s,%s,%s,%s,%s,%s)" % tuple(values)
    print("line 109: "+command);

    #try-expect block to test command (cursor.execute())
    try:
        cursor.execute(command);
    except Exception as e:
        print("line 115")
        print(e);
        return False;

    #execute command
    cursor.close()
    conn.commit();

    conn.close();
    return True;

#helper function that converts a dictionary keys/values into a string separated by commas
#It takes in a list essentially, adn converts its contents all into strings, each element separated
#by commas.
def add_helper(a):
    return (','.join([element for element in a ]))


#delete an entry from table t
def delete(d):
    pass

#search entries from the database database and returns a location? of the entry
def search(d):
    pass;

#update takes in an entry and updates it with a new entry
def update(d):
    pass;

def delete_table(table_name):
    #create conn and cursor objects
    conn=connect();
    cursor=conn.cursor()

    #execute drop table command: "DROP TABLE table_name"
    try:
        cursor.execute("DROP TABLE "+str(table_name));
    except Exception as e:
        print("line 152");
        print(e);
        return False;

    #commit command and close objects
    conn.commit();

    cursor.close()
    conn.close()