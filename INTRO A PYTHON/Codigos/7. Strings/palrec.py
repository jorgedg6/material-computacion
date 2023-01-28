
def espal_rec(p):

    #CASO BASE 1
    if len(p) == 1:         #Una letra
        return True         #Una palabra de 1 letra siempre es pal

    #CASO BASE 2
    elif len(p) == 2:       #Dos letras
        return p[0] == p[1] #Es pal si las dos letras son iguales

    #CASO RECURSIVO
    else:
        h = p[0]            #Primera letra
        t = p[len(p)-1]     #Ultima letra
        b = p[1:len(p)-1]   #Las letras del medio

        mp = espal_rec(b)   #Eh tu, dime si las letras del medio son pal
        if mp and (h == t):
            res = True
        else:
            res = False

        return res



x = espal_rec("reconocer")
print(x)

y = espal_rec("animal")
print(y)

z = espal_rec("radar")
print(z)

p = espal_rec("rallar")
print(p)
