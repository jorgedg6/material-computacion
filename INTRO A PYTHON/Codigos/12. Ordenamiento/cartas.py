'''
def porPintaYNumMan(e):
    n = e[0]
    p = e[1]

    #Los corazones seran los 100algo,
    #Las picas los 200algo, ...
    if p == "C":
        v = 100+n
    elif p == "P":
        v = 200+n
    elif p == "D":
        v = 300+n
    elif p == "T":
        v = 400+n

    return v

def ordenar_cartas(b):
    b.sort(key=porPintaYNumMan)
'''

def porPintaYNum(e):
    n = e[0]
    p = e[1]
    
    #Corazones el 0, picas el 1, ...
    if p == "C":
        np = 0
    elif p == "P":
        np = 1
    elif p == "D":
        np = 2
    elif p == "T":
        np = 3

    return np,n

def ordenar_cartas(b):
    b.sort(key=porPintaYNum)


#TEST
b = [[8,"P"],[9,"D"],[1,"T"],[8,"C"],
     [2,"P"],[5,"C"],[1,"C"],[7,"D"]]

print("Des:", b)
ordenar_cartas(b)
print("Ord:", b)



