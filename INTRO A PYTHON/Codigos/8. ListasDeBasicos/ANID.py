t = input("Texto? ")

#Lista de las palabras entre espacios
pe = t.split(" ")

np = len(pe)

#Si hay puntuacion, incrementar palabras
for p in pe:
    num = 0
    for i in range(0,len(p)):
        #Todos los signos que no son el ultimo caracter
        #esconden una palabra extra
        if p[i] in ".,:;" and i != len(p)-1:
            num += 1
    np += num

print(np,"Palabras")
    
    




