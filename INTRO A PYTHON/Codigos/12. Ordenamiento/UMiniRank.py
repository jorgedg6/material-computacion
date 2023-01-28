class Uni:
    def __init__(self,n,d,i,t):
        self.nom = n
        self.doc = d
        self.inv = i
        self.trans = t

    def __str__(self):
        return self.nom


sts = Uni("Sants University"    ,8,7,6)
oso = Uni("OsloTech"            ,6,9,6)
zom = Uni("University of Zoom"  ,3,4,3)
vit = Uni("VIT"                 ,8,9,8)
unis = [sts,oso,zom,vit]

#1 - Definir la funcion para key
def alGustoDeJorge(elem):
    puntos = (elem.doc*0.7) + (elem.trans*0.3)
    return puntos

#2- Ordenar descendentemente usando la key
unis.sort(key=alGustoDeJorge)
unis.reverse()

for i in range(0,len(unis)):
    print(i,"->",unis[i])



