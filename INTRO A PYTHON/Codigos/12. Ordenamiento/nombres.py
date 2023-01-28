#Leer archivo
r = open("nombres.txt")
ls = r.readlines()
r.close()

#Lista de nombres sin repetidos
ns = []
for l in ls:
    n = l.strip()
    if n not in ns:
        ns.append(n)
        
#Ordenar
ns.sort()

#Escribir archivo
e = open("nombresord.txt","w")
for n in ns:
    print(n,file=e)
e.close()


