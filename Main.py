from Database import *
from CSV import *
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
    #print(write("C:/Users/gupta/PycharmProjects/Pokemon.csv",[d]))
    #createCSV("Pokemon",d.values())
    #printCSV("Pokemon.csv")
    print(read("Pokemon.csv"));
    #printCSV("Pokemon.csv")

if(__name__ == '__main__'):
    csvTest();
