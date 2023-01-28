class Stack():
    def __init__(self):
        #Pista: usar una lista como atributo
        self.elems = []
    def push(self,e):
        #Ponerlo el ultimo
        self.elems.insert(len(self.elems),e)
    def pop(self):
        #Sacar el ultimo
        return self.elems.pop(len(self.elems)-1)
    def size(self):
        return len(self.elems)
        

class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None

def order_it(root):
    stack = Stack()

    dedo = root
    stack.push(dedo)

    while (stack.size() > 0):
        
        if dedo.left != None:
            stack.push(dedo.left)
            dedo = dedo.left

        else:
            dedo = stack.pop()
            print(dedo.value)
            if dedo.right != None:
                stack.push(dedo.right)
                dedo = dedo.right

def order_it_2(root):
    stack = Stack()
    dedo = root

    continuar = True
    while (stack.size() > 0 or dedo != None):
        if dedo != None:
            stack.push(dedo)
            dedo = dedo.left
        else:
            n = stack.pop()
            print(n.value)
            dedo = n.right
            
        
                

def order_rec(n):
    #CASO BASE: None (no hacer nada)
    #CASO RECURSIVO: Nodo normal
    if n != None:
        order_rec(n.left)
        print(n.value)
        order_rec(n.right)
        

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

#IMPRIMIR ORDENADOS
order_it_2(root)

