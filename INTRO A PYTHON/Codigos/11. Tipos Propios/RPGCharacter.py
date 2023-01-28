'''
#Crear una lista vacia
lista1 = []

#Agregar un elemento al final
lista1.append("cosa")

#Quita y retorna el elemento en la posicion 8
elem = lista1.pop(8)

#Crear un personaje
#Necesita un nombre y un tipo (WARRIOR o WIZARD)
#Si es WARRIOR tendra 50 puntos de vida inicial
#Si es WIZARD tendra 30 puntos de vida inicial
personaje1 = RPGCharacter("Gandalf","WIZARD")

#Infligir dano al personaje
#Necesita los puntos de dano
personaje1.damage(20)

#Retorna un entero con los puntos de vida
#actuales del personaje
vida1 = personaje1.life()

#Retorna un entero con los puntos de un ataque
#Numero al azar entre el min y el max del poder
#Si es WARRIOR sera entre 20 y 40
#Si es WIZARD sera entre 22 y 42
at1 = personaje1.attack()
'''



import random

class RPGCharacter:
    def __init__(self,n,c):
        self.c = c
        self.n = n
        if self.c == "WARRIOR":
            self.l = 50
        elif self.c == "WIZARD":
            self.l = 30

    def attack(self):
        if self.c == "WARRIOR":
            a = random.randint(20,40)
        elif self.c == "WIZARD":
            a = random.randint(22,42)
        return a

    def damage(self,d):
        self.l -= d

    def life(self):
        return self.l

#Martigan WARRIOR
#Willow WIZARD

#Creo Jugador 1
n1 = input("J1: Nombre? ")
t1 = input("J1: WARRIOR or WIZARD? ")
c1 = RPGCharacter(n1,t1)

#Creo Jugador 2
n2 = input("J2: Nombre? ")
t2 = input("J2: WARRIOR or WIZARD? ")
c2 = RPGCharacter(n2,t2)

#Let them fight!
continuar = True
while continuar:
    a1 = c1.attack()
    a2 = c2.attack()
    print(n1,"con",a1,"y",n2,"con",a2)

    #Jugador 1 Gana
    if a1 >= a2:
        d = a1-a2
        print(n2,"pierde",d,"puntos")
        c2.damage(d)
        print("--VIDA--",n1,c1.life(),n2,c2.life())
        if c2.life() <= 0:
            print(n2,"MUERE")
            continuar = False

    #Jugador 2 gana
    if a1 < a2:
        d = a2 - a1
        print(n1,"pierde",d,"puntos")
        c1.damage(d)
        print("--VIDA--",n1,c1.life(),n2,c2.life())
        if c1.life() <= 0:
            print(n1,"MUERE")
            continuar = False
    
    print("###")




