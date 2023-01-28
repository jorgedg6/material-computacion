class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None


def path(root,num):
    dedo = root

    continuar = True
    while continuar:
        print(dedo.value)

        if dedo.value == num:
            continuar = False

        elif dedo.value > num:
            if dedo.left == None:
                print("X")
                continuar = False
            else:
                dedo = dedo.left
        elif dedo.value < num:
            if dedo.right == None:
                print("X")
                continuar = False
            else:
                dedo = dedo.right



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

#IMPRIMIR PATHS
print("PATH 4")
path(root,4)

print("PATH 8")
path(root,8)

