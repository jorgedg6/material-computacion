
class HaciaSJ:
    def __init__(self,n,o):
        self.nom = n
        self.ori = o
        self.des = "San Joaquin"

    def __str__(self):
        t = "Trayecto "+self.ori+" a "+ self.des+" para "+self.nom
        return t


nom = input("Nombre? ")
origen = input("Origen? ")
v = HaciaSJ(nom,origen)
print(v)


        
        

