tr = open("LETtext.txt")
tls = tr.readlines()
tr.close()

cr = open("LETconectores.txt")
cls = cr.readlines()
cr.close()

#Crear list de str con conectores
#sin el ninja (\n)
cons = []
for cl in cls:
    cons.append(cl.strip())


unavez = []
repetidas = []
for tl in tls:
    p = tl.strip()
    if p not in cons:

        #Primera vez
        if p not in unavez:
            unavez.append(p)
        #Segunda vez
        elif p not in repetidas:
            repetidas.append(p)

for p in repetidas:
    print(p)









