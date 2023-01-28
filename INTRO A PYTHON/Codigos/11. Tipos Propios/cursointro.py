class CursoIntro:
    def __init__(self,i1,i2,ex):
        self.i1 = i1
        self.i2 = i2
        self.ex = ex
        self.nom = "IntroProgra"



#Pregunta (por input) los promedios
pi1 = float(input("Promedio I1: "))
pi2 = float(input("Promedio I2: "))
pex = float(input("Promedio Ex: "))

#Crea una variable de tipo Curso Intro
c = CursoIntro(pi1,pi2,pex)

pf = c.i1*0.25+c.i2*0.25+c.ex*0.5
print("El promedio final de",c.nom,"es",pf) 



