import random

class Geniom:
    def __init__(self,n):
        self.nom = n
        self.maxat = random.randint(1,5) 
        self.vida = 10

n1 = input("Geniom 1: ")
g1 = Geniom(n1)
print(g1.nom,"tiene",g1.vida,"de vida y", g1.maxat,"de ataque maximo")

n2 = input("Geniom 2: ")
g2 = Geniom(n2)
print(g2.nom,"tiene",g2.vida,"de vida y", g2.maxat,"de ataque maximo")

turno = 1
while (g1.vida > 0) and (g2.vida > 0):

    if turno == 1:
        at = random.randint(0,g1.maxat)
        print(g1.nom, "ataca con", at)
        g2.vida = g2.vida - at
        print("La vida de", g2.nom, "ahora es", g2.vida)
        turno = 2

    elif turno == 2:
        at = random.randint(0,g2.maxat)
        print(g2.nom, "ataca con", at)
        g1.vida = g1.vida - at
        print("La vida de", g1.nom, "ahora es", g1.vida)
        turno = 1

print("Combate acadado")
if g1.vida > 0:
    print("GANA", g1.nom)
elif g2.vida > 0:
    print("GANA", g2.nom)


