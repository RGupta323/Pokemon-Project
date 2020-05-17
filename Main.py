from Database import *
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
   d={"table-name":"Pokemon","name":"a", "types":"a", "abilities":"a", "height":1,
      "weight":1, "gender":"a", "evolution":"a"}
    #self.assertEqual(True, add(e, "Pokemon"))
   add(d);


if(__name__ == '__main__'):
    addTest();
