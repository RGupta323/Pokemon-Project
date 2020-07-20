'''Class to contain a node class for the tree class'''
class Node:
    #each node contains:
    #children: a list that contains other nodes that are its children
    # parent: which identifies the parent node that it belongs to
    #data: the data it contains.
    def __init__(self, data, parent, children: list=[]):
        self.parent=parent
        self.children=children;
        self.data = data

    def addChild(self, n):
        self.children.append(Node(parent=self, children=[], data=n));

    #gets teh ith child
    def getChild(self, i:int):
        return self.children[i];

    def deleteChild(self,i:int):
        try:
            self.children.remove(self.children[i])
        except Exception as e:
            print("Node.py, deleteChild(), line 25. Exception: {}. i value: {}, length of self.children: {}".format(e,i,len(self.children)))
            return False
        return True
    #function to delete all children of this node
    def deleteAllChildren(self):
        self.children=list()

    def equals_strict(self, n):
        self.children.sort()
        n.children.sort()
        return (self.data==n.data) and (self.parent==n.parent) and (self.children==n.children)

    #regular equals method, not strict, just comparing the data
    def equals(self,n):
        return self.data==n.data;

    #toString() method
    def toString(self):
        return self.data

