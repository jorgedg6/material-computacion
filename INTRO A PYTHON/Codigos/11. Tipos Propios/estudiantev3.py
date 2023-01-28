class Estudiante:
    def __init__(self,nom, i1,i2,ex):
        self.nom = nom
        self.i1 = i1
        self.i2 = i2
        self.ex = ex

    def supera_d(self,t):
        n = (self.i1 * 0.25) + (self.i2 * 0.25) + (self.ex * 0.5)
        if n >= t:
            res = True
        else:
            res = False
        return res

    def calcular_nota(self):
        n = (self.i1 * 0.25) + (self.i2 * 0.25) + (self.ex * 0.5)
        return n

    def supera(self,t):
        n = self.calcular_nota()
        if n >= t:
            res = True
        else:
            res = False
        return res



e1 = Estudiante("Alice",4.0,4.0,4.0)
e2 = Estudiante("Bob",6.0,4.0,5.0)

t1 = 3.5
t2 = 4.5

print(e1.nom,"supera", t1,"?", e1.supera(t1))
print(e1.nom,"supera", t2,"?", e1.supera(t2))
print(e2.nom,"supera", t1,"?", e2.supera(t1))
print(e2.nom,"supera", t2,"?", e2.supera(t2))




