ns = []
ds = []
ms = []

continuar = True
while continuar:

    n = input("Nombre: ")
    d = int(input("Dia: ")) #Si no pones int, 07 y 7 no es lo mismo
    m = int(input("Mes: "))

    #Mirar si hay coincidencia
    esta = False
    for i in range(0,len(ns)):
        if (ds[i] == d) and (ms[i] == m):
            print("COINCIDENCIA")
            print(n,"y",ns[i],"tienen el cumple el",d,"del",m)
            continuar = False
            esta = True

    if not esta:
        ns.append(n)
        ds.append(d)
        ms.append(m)

print("Has necesitado", len(ns)+1, "personas")
    




