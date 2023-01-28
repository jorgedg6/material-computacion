class Estudiante:
    def __init__(self,i1,i2,ex):
        self.i1 = i1
        self.i2 = i2
        self.ex = ex


def calcular_nota(e):
    n = (e.i1 * 0.25) + (e.i2 * 0.25) + (e.ex * 0.5)
    return n



#TEST
e1 = Estudiante(4.0,4.0,4.0)
print(calcular_nota(e1))

e2 = Estudiante(4.0,4.0,6.0)
print(calcular_nota(e2))



bob = Estudiante(4.0,4.0,6.0)

nota = (bob.i1 * 0.25) + (bob.i2 * 0.25) + (bob.ex * 0.5)
print("La nota de Bob es", nota)



