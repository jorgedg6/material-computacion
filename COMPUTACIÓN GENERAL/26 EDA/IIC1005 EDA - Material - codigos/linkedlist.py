class Node:
    def __init__(self,d):
        self.data = d
        self.next = None


def agregar_despues_B(head,e):
    dedo = head
    
    #Encontrar el nodo antes de C
    while dedo.next.data != "C":
        dedo = dedo.next

    #Pre y post
    pre = dedo #El antes de la C
    post = dedo.next #C
        
    #Empalmar
    n = Node(e)
    pre.next = n
    n.next = post  


#EJEMPLO LINKED LIST
#Nodes
na = Node("A")
nb = Node("B")
nc = Node("C")
nd = Node("D")
#Encadenar
na.next = nb
nb.next = nc
nc.next = nd
#Head
head = na

#IMPRIMIR EJEMPLO
print("IMPRIMIR EJEMPLO")
dedo = head
while dedo != None:
    print(dedo.data)
    dedo = dedo.next

#AGREGAR ELEM DESPUES DE B
agregar_despues_B(head,"E")

#IMPRIMIR EJEMPLO CON E
print("IMPRIMIR EJEMPLO CON E ANTES DE C") 
dedo = head
while dedo != None:
    print(dedo.data)
    dedo = dedo.next
