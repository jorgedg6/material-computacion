import random

class Geniom:
    def __init__(self,n):
        self.nom = n
        self.at = random.randint(1,5)
        self.vida = random.randint(10,20)

n1 = input("Geniom 1: ")
n2 = input("Geniom 2: ")

g1 = Geniom(n1)
g2 = Geniom(n2)

print(g1.nom,"=> Vida:",g1.vida, "Ataque:",g1.at)
print(g2.nom,"=> Vida:",g2.vida, "Ataque:",g2.at)

turno = 1
while (g1.vida > 0) and (g2.vida > 0):

    if turno == 1:
        print("Ataca", g1.nom, "con", g1.at)
        g2.vida = g2.vida - g1.at
        print("Vida de", g2.nom, "ahora es", g2.vida)
        turno = 2

    elif turno == 2:
        print("Ataca", g2.nom, "con", g2.at)
        g1.vida = g1.vida - g2.at
        print("Vida de", g1.nom, "ahora es", g1.vida)
        turno = 1

print("Combate acadado")
if g1.vida > 0:
    print("GANA", g1.nom)
elif g2.vida > 0:
    print("GANA", g2.nom)


