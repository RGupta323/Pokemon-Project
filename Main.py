import sys;

from Data.Database import *
from Data.CSV import *;
from Data.WebScrape import *;

sys.path.insert(1, "C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Data\\CSV.py")
sys.path.insert(1,'C:\\Users\\gupta\\PycharmProjects\\PokemonProject\\Data\\Database.py')

#from Data.WebScrape import *
"""d=dict();
d={"id":1, "name":"a","types":"a","abilities":"a","height":1, "weight": 1,
   "gender":"a","evolution":"a"}
create_table("Pokemon",d);

conn=connect();
cursor=conn.cursor();
#cursor.execute("SELECT table_name FROM information_schema.tables  ")
cursor.execute("SELECT * FROM Pokemon");
for table in cursor.fetchall():
    print(table);
cursor.close()
conn.close(); """

def addTest():
   d={"table-name":"Pokemon","id":'1',"name":'a', "types":'a', "abilities":'a', "height":'1',
      "weight":'1', "gender":'a', "evolution":'a'}
    #self.assertEqual(True, add(e, "Pokemon"))
   #delete_table("Pokemon")
   #create_table("POKEMON",["id","name","types","abilities","height","weight","gender","evolution"])
   add(d);

def csvTest():
    #createCSV("Pokemon",["id","name","types","abilities","height","weight","gender","evolution"])
    d = {"id": '1', "name": 'a', "types": 'a', "abilities": 'a', "height": '1',
         "weight": '1', "gender": 'a', "evolution": 'a'}
    #print(write("Pokemon.csv",[d]))
    #createCSV("Pokemon",d.values())
    #printCSV("Pokemon.csv")
    #print(read("Pokemon.csv"));
    #printCSV("Pokemon.csv")
    print(checkCSV("Files/Pokemon.csv"))

def WebScraperTest():
    url="https://pokemondb.net/pokedex/national#gen-1"
    print(parse(url,id="gen-1"))

if(__name__ == '__main__'):
    WebScraperTest();
