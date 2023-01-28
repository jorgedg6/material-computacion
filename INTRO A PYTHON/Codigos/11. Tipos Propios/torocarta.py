class ToroCarta:
    def __init__(self,n):
        self.num = n

    def calcular_puntos(self):
        if self.num == 55:
            p = 7
        elif self.num % 11 == 0:
            p = 5
        elif self.num % 10 == 0:
            p = 3
        elif self.num % 5 == 0:
            p = 2
        else:
            p = 1
        return p

    def al_lado(self,n):
        if self.num == n+1 or self.num == n-1:
            r = True
        else:
            r = False
        return r

    def __str__(self):
        p = self.calcular_puntos()
        t = str(self.num)+"("+str(p)+")"
        return t


c55 = ToroCarta(55)
x = c55.al_lado(28)
y = c55.al_lado(54)
z = c55.al_lado(56)

print("55 al lado de 28?",x)
print("55 al lado de 54?",y)
print("55 al lado de 56?",z)


c55 = ToroCarta(55)
c11 = ToroCarta(11)
c23 = ToroCarta(23)

print(c55)
print(c11)
print(c23)
        

print("Carta",55,"tiene",c55.calcular_puntos(),"puntos")
print("Carta",11,"tiene",c11.calcular_puntos(),"puntos")
print("Carta",23,"tiene",c23.calcular_puntos(),"puntos")

