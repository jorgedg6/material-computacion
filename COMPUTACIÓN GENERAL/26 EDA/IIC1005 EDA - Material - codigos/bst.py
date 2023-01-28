class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

# EJEMPLO BST
#Nodes
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n10 = Node(10)
#Arcs
n3.left = n2
n3.right = n6
n6.left = n4
n6.right = n10
n4.right = n5
n10.left = n7
#Root
root = n3


#IMPRIMIR 5
n = root.right.left.right
print(n.value)


