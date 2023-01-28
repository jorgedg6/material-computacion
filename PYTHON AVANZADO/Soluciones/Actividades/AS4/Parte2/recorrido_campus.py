from Parte2.campus import Lugar
from collections import deque

def comprobar_chismoso(lugar: Lugar):
    # NO MODIFICAR
    for ayudante in lugar.ayudantes:
        if "Croak" in ayudante.frase:
            return True
    return False


def bfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    cola = deque()
    cola.append(inicio)
    visitados = set()

    while len(cola) > 0:
        lugar_actual = cola.popleft()
        #yield lugar_actual
        visitados.add(lugar_actual)
        if lugar_actual == final:
            return True
        
        for vecino in lugar_actual.vecinos:
            if not comprobar_chismoso(vecino) and vecino not in visitados:
                cola.append(vecino)
    return False


def dfs_iterativo(inicio: Lugar, final: Lugar):
    # Completar
    stack = deque()
    stack.append(inicio)
    visitados = set()

    while len(stack) > 0:
        lugar_actual = stack.pop()
        #yield lugar_actual
        visitados.add(lugar_actual)
        if lugar_actual == final:
            return True
        
        for vecino in lugar_actual.vecinos:
            if not comprobar_chismoso(vecino) and vecino not in visitados:
                stack.append(vecino)
    return False

def bfs_iterativo_largo(inicio: Lugar, final: Lugar):
    '''# Completar
    cola = deque()
    cola.append(inicio)
    visitados = set()
    largo = 0
    while len(cola) > 0:
        #Se extrae el primer elemento de la cola
        lugar_actual = cola.popleft()
        #Definimos que no posee vecinos factibles
        vecinos = False
        #Lo agregamos a los lugares visitados
        visitados.add(lugar_actual)
        #Verificamos si llegamos al final
        if lugar_actual == final:
            return largo
        #Por cada vecino comprobamos si tiene chismosos
        for vecino in lugar_actual.vecinos:
            if not comprobar_chismoso(vecino) and vecino not in visitados:
                #Agregamos los vecinos a la cola
                cola.append(vecino)
                #Definimos que el lugar actual si posee vecinos factibles
                vecinos = True
        #Si posee vecinos seguimos el camino
        if vecinos:
            largo += 1
    return -1'''
    pass

def dfs_iterativo_largo(inicio: Lugar, final: Lugar):
    # Completar
    stack = deque()
    stack.append(inicio)
    visitados = set()
    camino = []
    while len(stack) > 0:
        #Se extrae el primer elemento de la cola
        lugar_actual = stack.pop()
        #Definimos que no posee vecinos factibles
        vecinos = False
        #Lo agregamos a los lugares visitados
        visitados.add(lugar_actual)
        #Verificamos si llegamos al final
        if lugar_actual == final:
            return len(camino)
        #Por cada vecino comprobamos si tiene chismosos
        for vecino in lugar_actual.vecinos:
            if not comprobar_chismoso(vecino) and vecino not in visitados:
                #Agregamos los vecinos a la cola
                stack.append(vecino)
                #Definimos que el lugar actual si posee vecinos factibles
                vecinos = True
        #Si posee vecinos seguimos el camino
        if vecinos:
            camino.append(lugar_actual)
        else:
            #Sacamos el vertice que nos llevo
            camino.pop()
    return -1


def bfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres[inicio] = None

    # Completar
    pass

def dfs_iterativo_camino(inicio: Lugar, final: Lugar):
    # Utiliza este diccionario para implementar el camino. 
    # Las llaves del diccionario es UN nodo vecino (NO un listado de todos los nodos vecinos) 
    # y el valor el nodo en cuestion
    padres = dict()
    padres = dict()
    padres[inicio] = None

    # Completar
    pass
    
    
def creador_camino(diccionario_padres, final):
    # NO MODIFICAR
    camino = []
    camino.append(final)
    while diccionario_padres[final] is not None:
        camino.append(diccionario_padres[final])
        final = diccionario_padres[final]
    camino.reverse()
    return camino


def imprimir_camino(camino):
    # NO MODIFICAR
    recorrido = ""
    largo = len(camino)
    contador = 1
    for lugar in camino:
        if contador < largo:
            recorrido = recorrido + f"[{lugar.nombre}] -> "
        else:
            recorrido = recorrido + f"[{lugar.nombre}]."
        contador += 1
    print(recorrido)

if __name__ == "__main__":
    print("\nNO DEBES EJECUTAR AQUÍ EL PROGRAMA!!!!")
    print("Ejecuta el main.py\n")
    raise(ModuleNotFoundError)
