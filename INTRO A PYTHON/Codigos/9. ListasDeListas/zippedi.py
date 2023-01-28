def zippedi(m):

    nfilas = len(m)
    ncols = len(m[0])
    #Num de elementos de cualquier fila
    #por ejemplo, la 0

    #Buscar donde esta el robot y el producto
    for f in range(0,nfilas):
        for c in range(0,ncols):
            if m[f][c] == "R":
                rf = f
                rc = c
            elif m[f][c] == "P":
                pf = f
                pc = c

    #Naranjas
    nar = rc-pc
    #Puede ser pos o neg dependiendo de si el
    #robot esta a la izq o derecha del produc
    #Si es neg lo hacemos pos (mult por -1)
    if nar < 0:
        nar =  nar * -1

    #Rojas
    nro = rf - pf
    if nro < 0:
        nro = nro * -1

    tiempo = nar*1 + nro*2
    return tiempo
    


m = [["_","R","_","_","_"],
     ["_","_","_","_","P"],
     ["_","_","_","_","_"]]

print(zippedi(m))
