class EstudianteIntro:
    def __init__(self,i,ex,t,p):
        self.i = i
        self.ex = ex
        self.t = t
        self.p = p

    def nota_final(self):
        condt = self.t >= 4.0
        conde = self.i * 0.5 + self.ex * 0.5 >= 4.0
        nota = self.i*0.3 + self.ex*0.3 + self.t*0.3 + self.p*0.1
        
        if condt and conde:
            final = nota
        else:
            if nota < 3.9:
                final = nota
            else:
                final = 3.9

        return final

    def pasa(self):
        final = self.nota_final()
        if final >= 4.0:
            pasa = True
        else:
            pasa = False
        return pasa

    def supera(self,n):
        final = self.nota_final()
        if final >= n:
            supera = True
        else:
            supera = False
        return supera
        


e1 = EstudianteIntro(6.0,6.0,4.0,4.0)
n1 = e1.nota_final()
print(n1)
p1 = e1.pasa()
print(p1)
s1 = e1.supera(5.0)
print(s1)

e2 = EstudianteIntro(6.0,6.1,3.5,5.3)
n2 = e2.nota_final()
print(n2)
p2 = e2.pasa()
print(p1)
s2 = e2.supera(5.0)
print(s2)

e3 = EstudianteIntro(4.0,4.0,4.0,1.0)
n3= e3.nota_final()
print(n3)
p3 = e3.pasa()
print(p3)
s3 = e3.supera(5.0)
print(s3)



