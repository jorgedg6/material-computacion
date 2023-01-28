def hijos(a,n):
    res = []

    #Recorrer hasta encontrar la persona (n)
    for p in a:
        nombre = p[0]

        #Si es la persona que busco
        if nombre == n:
            #Lista de posiciones de los hijos
            phs = p[1]

            #Por cada pos de cada hijo
            for ph in phs:
                nombre = a[ph][0]
                res.append(nombre)

    return res
    

def padres(a,n):
    #Buscar la posicion de la persona
    for i in range(len(a)):
        nombre = a[i][0]
        if nombre == n:
            pos = i

    #Buscar gente que tiene pos en sus hijos
    res = []
    for p in a:
        nom = p[0]
        phjs = p[1]
        if pos in phjs:
            res.append(nom)

    return res

lista = [
    ["Abraham",[1,2]], #0
    ["Herb",[]], #1
    ["Homero",[3,4,5]], #2
    ["Bart",[]], #3
    ["Maggie",[]], #4
    ["Lisa",[]], #5
    ["Marge",[3,4,5]], #6
    ["Mona",[1,2]], #7
    ["Clancy",[6,10,11]], #8
    ["Jackie",[6,10,11]], #9
    ["Selma",[12]], #10
    ["Patty",[]], #11
    ["Ling",[]] #12
    ]

print(lista)
print(hijos(lista,"Marge"))
print(hijos(lista,"Clancy"))
print(hijos(lista,"Maggie"))

print(padres(lista,"Maggie"))
print(padres(lista,"Homero"))
print(padres(lista,"Ling"))
print(padres(lista,"Abraham"))
        

