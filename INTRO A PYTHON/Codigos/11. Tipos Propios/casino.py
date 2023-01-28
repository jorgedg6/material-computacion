class Colacion:
    def __init__(self):
        self.fondo = ""
        self.agre = ""
        self.doble = ""
        self.postre = ""

    def precio(self):
        p = 1600 #Fondo + agregado
        if self.doble:
            p += 300
        if self.postre != "":
            p += 600
        return p

    def __str__(self):
        t = self.fondo + " con "
        if self.doble:
            t += "doble de "
        t += self.agre
        if self.postre != "":
            t += " y " + self.postre
        return t


#NUEVA COLACION
c = Colacion()

c.fondo = input("Que Fondo? ")
c.agre = input("Que Agregado? ")

d = int(input("Quiere doblar agregado? 1-Si 2-No: "))
if d == 1:
    c.doble = True
else:
    c.doble = False

q = int(input("Quiere postre? 1-Si 2-No: "))
if q == 1:
    c.postre = input("Que postre? ")

print("Su colacion es", c)
print("Precio: ", c.precio())




