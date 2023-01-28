'''
def inverso_rec(p):

    #CASO BASE
    if len(p) == 1:         #Una letra
        return p            #La misma palabra

    #CASO RECURSIVO
    else:
        h = p[0]            #La primera letra
        b = p[1:]           #El resto de letras

        x = inverso_rec(b)  #Eh tu, dame el inverso
        r = x + h           #Pongo la letra al final
        return r

'''

def inverso_rec(p):
    if len(p) == 1:
        return p
    else:
        return inverso_rec(p[1:])+p[0]


x = inverso_rec("aeiou")
print(x)

y = inverso_rec("animal")
print(y)

z = inverso_rec("radar")
print(z)





