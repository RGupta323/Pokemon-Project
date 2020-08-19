import unittest
from Objects.Node import *
from Data.JSON import *

class MyTestCase(unittest.TestCase):
    #sample test
    def test_something(self):
        self.assertEqual(True, True)

    #first node test
    def test_addChild(self):
        path="C://Users//gupta//PycharmProjects//PokemonProject//Files//Pokemon//"
        data = read(path+"blastoise.json");
        data = json.loads(data)
        self.assertEqual(type(data),dict);
        #print(data)
        #self.assertEqual(type(json.loads(data)), dict)
        n = Node(parent=None, children=[], data=data['abilities'])
        print("first node created!")
        self.assertEqual(n.data, data['abilities'])

        for element in n.data:
            n.addChild(element)
        print([element.data for element in n.children])
        print("length of n.children: {}".format(len(n.children)))
        print("n.children: {}".format(n.children))
        while(len(n.children)!=0):
            n.deleteChild(0);
        self.assertEqual(n.children, list())


    def test_equalsTest(self):
        path = "C://Users//gupta//PycharmProjects//PokemonProject//Files//Pokemon//"
        data = read(path + "blastoise.json");
        data = json.loads(data)
        self.assertEqual(type(data), dict);
        # print(data)
        # self.assertEqual(type(json.loads(data)), dict)
        n = Node(parent=None, children=[], data=data['abilities'])
        self.assertEqual(n.data, data['abilities'])
        for element in n.data:
            n.addChild(element)

        self.assertEqual(len(n.children), 2)

        for i in range(len(n.children)):
            self.assertEqual(n.children[i].equals(n), False)

        j=0;
        for child in n.children:
            self.assertEqual(child.equals(n.children[j]),True)
            j+=1


if __name__ == '__main__':
    unittest.main()
