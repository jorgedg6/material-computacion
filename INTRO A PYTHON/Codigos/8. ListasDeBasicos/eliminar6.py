def eliminar6(x):
    i = 0
    while i < len(x):
        if x[i] == 6:
            x.pop(i)
        i += 1
    return x

p = [5,2,5,7,6,3,6]
q = eliminar6(p)
print(q)
        


p = [5,6,6,6,6,3,6]
q = eliminar6(p)
#print(q)


def eliminar6buena(x):
    r = []
    for e in x:
        if e != 6:
            r.append(e)
    return r


p = [5,6,6,6,6,3,6]
q = eliminar6buena(p)
#print(q)

def eliminar6cuidado(x):
    i = 0
    while i < len(x):
        if x[i] == 6:
            x.pop(i)
        else:
            i += 1
    return x

p = [5,6,6,6,6,3,6]
q = eliminar6cuidado(p)
print(q)
