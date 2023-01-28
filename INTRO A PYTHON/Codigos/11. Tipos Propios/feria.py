class Stand:
    def __init__(self):
        self.titulo = ""
        self.par = 0

    def titulo(self):
        return self.titulo

    def participantes(self):
        return self.par

    def vacio(self):
        return self.par == 0



class Feria:
    def __init__(self, ns):
        self.stands = []
        for i in range(0,ns):
            s = Stand()
            self.stands.append(s)

    def inscribir(self,t,p):
        i = 0
        inscrito = False
        while not inscrito:
            s = self.stands[i]
            if s.vacio():
                s.titulo = t
                s.par = p
                inscrito = True
            i += 1

    def obtener_stand(self, n):
        return self.stands[n]

    def numero_stands_vacios(self):
        vacios = 0
        for s in self.stands:
            if s.vacio():
                vacios += 1
        return vacios

    def quedan_stands_vacios(self):
        return self.numero_stands_vacios() > 0
            










        


#CODIGO PRINCIPAL
ns = int(input("Numero stands en la Feria: "))
f = Feria(ns)

op = int(input("1-Inscribir 2-Info 3-Cerrar: "))
while op != 3:

    if op == 1:
        if f.quedan_stands_vacios():
            t = input("Titulo del stand: ")
            p = int(input("Numero de participantes del stand: "))
            f.inscribir(t,p)
        else:
            print("No quedan stands vacios")

    elif op == 2:
        n = int(input("Numero de stand: "))
        s = f.obtener_stand(n) #s de tipo Stand
        if s.vacio():
            print("Stand vacio")
        else:
            print("Titulo =>", s.titulo())
            print("Participantes =>", s.participantes())
        
    op = int(input("1-Inscribir 2-Info 3-Cerrar: "))

print("Feria Cerrada")
print("Quedaron", f.numero_stands_vacios(), "stands por llenar")



