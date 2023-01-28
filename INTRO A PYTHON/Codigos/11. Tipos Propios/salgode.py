class Peticion:
    def __init__(self,nom,ori,des):
        self.n = nom
        self.o = ori
        self.d = des


pet = []

op = int(input("1-Peticion 2-SalgoDe 3-Stats 0-Salir: "))
while op != 0:

    if op == 1:
        n = input("Nombre: ")
        o = input("Origen: ")
        d = input("Destino: ")
        p = Peticion(n,o,d)
        pet.append(p)
        
    elif op == 2:
        o = input("Origen: ")
        d = input("Destino: ")
        v = int(input("Vacantes: "))

        l = v
        i = 0
        ocu = []
        while l>0 and i>len(pet):
            p = pet[i]
            if p.o == o and p.d == d:
                ocu.append(p.n)
                pet.pop(i)
                l = l -1
            else:
                i += 1
        print("Llevarse a", ocu)

    elif op == 3:
        print("Peticiones actuales", len(pet))

    op = int(input("1-Peticion 2-SalgoDe 3-Stats 0-Salir: "))

print("PROGRAMA ACABADO")
        

