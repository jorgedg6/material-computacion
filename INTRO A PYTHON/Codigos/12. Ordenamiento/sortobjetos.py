class Persona:
    def __init__(self,n,a,e):
        self.nom = n
        self.ape = a
        self.edad = e
        
    def __str__(self):
        t = self.nom+" "+self.ape+" ("+str(self.edad)+")"
        return t


p1 = Persona("Carlos","Barranco",15)
p2 = Persona("Anna","Caceres",22)
p3 = Persona("Benjamin","Alvarez",38)
q = [p1,p2,p3]

#1 - Definir la funcion para key
def porNombre(elem):
    return elem.nom



#1 - Definir la funcion para key
def porApeYLuegoNombre(elem):
    return elem.ape,elem.nom





#1 - Definir la funcion para key
def porApellido(elem):
    return elem.ape

#1 - Definir la funcion para key
def porEdad(elem):
    return elem.edad

#1 - Definir la funcion para key
def porNumLetras(elem):
    num = len(elem.nom)
    return num

#1 - Definir la funcion para key
def porVocalDif(elem):
    vocales = []
    for c in elem.nom:
        c = c.lower()
        if (c in "aeiou") and (c not in vocales):
            vocales.append(c)
    return len(vocales)

#2- Ordenar usando la key
q.sort(key=porVocalDif)

print("0->",q[0])
print("1->",q[1])
print("2->",q[2])

