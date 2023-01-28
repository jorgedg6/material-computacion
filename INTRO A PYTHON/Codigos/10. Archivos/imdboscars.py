r = open("IMDBtitles.txt")
ls = r.readlines()
r.close()

# Lista de pelis, donde cada peli es
# una list [nom,num] 
pelis = []

#Crear esta lista de pelis y nums
for l in ls:
    nom = l.strip()

    #Mirar si esta
    #Y si esta incrementar
    esta = False
    for peli in pelis:
        if peli[0] == nom:
            peli[1] += 1
            esta = True

    #Si no esta la creo y la agrego
    if not esta:
        x = [nom,1]
        pelis.append(x)


#Buscar la mas votada
maxnum = -1
maxnom = ""
for peli in pelis:
    if peli[1] > maxnum:
        maxnum = peli[1]
        maxnom = peli[0]

print("Ganador:",maxnom,"con",maxnum,"votos")









