class EstudianteIntro:
    def __init__(self,i,ex,t,p):
        self.i = i
        self.ex = ex
        self.t = t
        self.p = p

    def pasa(self):
        pasa = True
        if self.t < 4.0:
            pasa = False
        elif (self.i * 0.5 + self.ex * 0.5) < 4.0:
            pasa = False
        elif (self.i*0.3 + self.ex*0.3 + self.t*0.3 + self.p*0.1) < 4.0:
            pasa = False
        return pasa

    def mensaje_adecuado(self):
        if self.pasa():
            m = "Felicidades"
        else:
            m = "Mala suerte"
        return m


e1 = EstudianteIntro(6.0,6.0,4.0,4.0)
p1 = e1.pasa()
print(p1)
t1 = e1.mensaje_adecuado()
print(t1)

e2 = EstudianteIntro(6.0,6.1,3.5,5.3)
p2 = e2.pasa()
print(p2)
t2 = e2.mensaje_adecuado()
print(t2)

e3 = EstudianteIntro(4.0,4.0,4.0,1.0)
p3 = e3.pasa()
print(p3)
t3 = e3.mensaje_adecuado()
print(t3)



