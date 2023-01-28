def conectado(g):

    pms = [] #personas Por Mirar
    yms = [] #personas Ya Miradas

    #Partire mirando la persona 0
    pms.append(0)

    #Mientras tenga personas por mirar ...
    while len(pms) > 0:

        # Saco a la persona de la lista por mirar
        p = pms.pop()
        # La Pongo en la lista de ya mirados
        yms.append(p)

        #Voy a mirar personas con quien se relaciona
        #Pero solo interesa si no la he mirado ya
        #o no la tengo ya en la lista por mirar
        rel = g[p]
        for i in range(0,len(rel)):
            if (rel[i] == True) and (i not in pms) and (i not in yms):
                pms.append(i)
        

    #Si el num de personas miradas son todas esta conectado
    return len(yms) == len(g)
         

gc = [[False,True,True],
      [True,False,False],
      [True,False,False]]

print(conectado(gc))

gd = [[False,True,False],
      [True,False,False],
      [False,False,False]]

print(conectado(gd))
