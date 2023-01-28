er = open("fiestaest.csv")
els = er.readlines()
er.close()

hr = open("fiestahoy.csv")
hls = hr.readlines()
hr.close()

#Calcular estadisticas
stats = []
for l in els:
    cs = l.strip().split(";")
    n = cs[0]
    tics = cs[1:]
    suma = 0
    for tic in tics:
        if tic == "X":
            suma += 1
    pro = suma / len(tics)
    stat = [n,pro]
    stats.append(stat)

#Calcular el numero de personas
res = 0
for l in hls:
    n = l.strip()

    #Buscar si esta
    esta = False
    for stat in stats:
        if stat[0] == n:
            res += stat[1]
            esta = True

    if not esta:
        res += 1

print("Num previsto:",res)
    
    
    





