#Python file for all database functions
from databases import Database;
import mysql.connector;
import psycopg2;
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


#add data to the database to a specific table t
def add(data,table_name):
    if(table_name not in tables):
        return None;

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
#Where d is a dictionary, its keys are the attributes or columsn of the table,
#and the values are the types of each column
#example: {id:1, name:varchar(255)}
#strings are varchar(255), ints are int,
def create_table(table_name, d):
    conn=connect();
    if(conn==None):
        return None;
    cursor=conn.cursor();
    a=str();
    for i in range(len(list(d.keys()))):
        key=list(d.keys())[i]
        #determien b
        b=str()
        if(type(d[key])==int):
            b="int";
        elif(type(d[key])==str):
                b="varchar(255)"
        #create a
        if(i==len(list(d.keys()))-1):
            a+=str(key)+" "+str(b)+"\n";
        else:
            a+=str(key)+" "+str(b)+",\n"
    #print(a);
    cursor.execute("""CREATE TABLE """+str(table_name)+"""( """+a+""");""")
    #cursor.commit();
    #print(cursor.fetchall());
    cursor.close();
    conn.commit(); 
    conn.close();


#delete an entry from the database from a specific table t
def add(entry, table_name):
    pass;

#search entries from the database database and returns a location? of the entry

#update takes in an entry and updates it with a new entry