import time

class Caso:
    
    def __init__(self,cid,edad):
        self.cid = cid
        self.edad = edad
        self.res = -1
        self.tini = time.time()
        self.tfin = -1

cs = []

#Abre un nuevo caso antes de haer el analisis
#Recibe un int con la edad del paciente
#Retorna un int con el identificador del caso
def abrir(edad):
    cid = len(cs)
    c = Caso(cid,edad)
    cs.append(c)
    return cid

#Cierra el caso registrando el resultado del analisis
#Recibe un int con el identificador del caso
#y un int con el resultado (0-Neg o 1-Pos)
#No retorna nada
def cerrar(cid,res):
    c = cs[cid]
    c.res = res
    c.tfin = time.time()

#Retorna el numero de casos abiertos
#No recibe nada.
#Retorna un int con el numero de casos
#Nota: los caso se identifican con un int del 0 al ncasos-1
def ncasos():
    return len(cs)

#Retorna la edad del paciente del caso
#Recibe un int con el identificador del caso
#Retorna un int con la edad del caso
def edad(cid):
    return cs[cid].edad

#Retorna el resultado del analisis del caso
#Recibe un int con el identificador del caso
#Retorna un int con el resultado: Neg(0), Pos(1), Sin Resultado(-1) 
def resultado(cid):
    return cs[cid].res


