import collections


class Node:
    def __init__(self, number):
        self.number = number
        self.root=None
        self.left=None
        self.right=None


 
class Tree:
    def __init__(self, node):
        self.nodes = Node(node.number) ###!!!

    def Add(self,node):
        if self.nodes.left == None or self.nodes.right == None:
            if node.nodes.number!=0:
                if node.nodes.left==None:
                    self.nodes.left=node
                    node.nodes.root = self
                else:
                    self.nodes.left.Add(node)
            #else:
                #self.nodes.right=node
                #node.nodes.root = self
        else:
            if self.nodes.root != None:
                self.nodes.root.Add(node)








###
def InorderTreeWalk(x):
    if x.number != None:
        InorderTreeWalk(x.left)
        print(x)
        InorderTreeWalk(x.right)

def TreeSearch(x, k):
        if x.number == None or k == x.number:
            return x
        if k < x.number:
            return TreeSearch(x.left, k)
        else:
            return TreeSearch(x.right, k)

def IterativeTreeSearch(x, k):
    while x != None and k != x.number:
        if k < key[x]:
            x = left[x]
        else:
            x = right[x]
        return x

def TreeMinimum(x):
    while x.left != None:
        x = x.left
    return x

def TreeMaximum(x):
    while x.left != None:
        x = x.right
    return x
###

array=[1, 4, 6, 10, 0, 0, 0, 7, 0, 8, 0, 0, 2, 5, 0, 0, 3, 9, 0, 0, 0]
tree1 = Tree(Node(array[0]))
for i in range(1,len(array)):
    tree1.Add(Node(array[i]))
