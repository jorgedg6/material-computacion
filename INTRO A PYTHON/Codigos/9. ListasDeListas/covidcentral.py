def maxrel(g):
    np = len(g) #Numero de personas

    maxp = -1 #Numero de la persona con mas rel
    maxn = -1 #Numero de rels de la persona con mas

    #Para cada persona mirar cuantas relaciones
    for i in range(0,np):

        #Contar su numero de Trues
        rel = g[i]
        numT = 0
        for r in rel:
            if r == True:
                numT += 1

        #Mirar si es mayor que lo que llevaba
        if numT > maxn:
            maxn = numT
            maxp = i

    return maxp
         



g = [[False,True,True,False,False,False,False,False],
     [True,False,False,True,False,True,False,False],
     [True,False,False,False,False,True,False,False],
     [False,True,False,False,False,True,False,False],
     [False,False,False,False,False,True,False,False],
     [False,True,True,True,True,False,True,True],
     [False,False,False,False,False,True,False,True],
     [False,False,False,False,False,True,True,False]]

print(maxrel(g))
