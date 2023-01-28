r = open("Extendido.csv")
ls = r.readlines()
r.close()

datos = []
for l in ls[1:]:
    cs = l.strip().split(",")

    esta = False
    for dato in datos:
        if dato[0] == cs[4]:
            dato[2] += 1
            esta = True

    if not esta:
        dato = [cs[4],cs[6],1]
        datos.append(dato)


e = open("facnum.csv","w")

print("CODE","FAC","NUM", sep=",", file=e)
for d in datos:
    #sep nos sirve poner un str entre los
    #elementos a imprimir
    print(d[0],d[1],d[2],sep=",",file=e)

e.close()



