#Define la clase HaciaSJ
class HaciaSJ:
    def __init__(self,n,o):
        self.nom = n
        self.ori = o
        self.des = "San Joaquin"


nom = input("Nombre? ")
origen = input("Origen? ")

#Crea una variable de tipo HaciaSJ
v = HaciaSJ(nom,origen)

print(v.nom,"necesita ir de",v.ori,"a",v.des)


        
        

