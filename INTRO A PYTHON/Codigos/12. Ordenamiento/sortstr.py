p = ["raton","botella","taza","camara","ventana","libro"]
print("Antes: ", p)

def porAs(e):
    numA = 0
    for c in e:
        if c == "a":
            numA += 1
    return numA

p.sort(key=porAs)

print("Despues: ", p)





p = ["casa","caracol","Barco","Arbol","Auto","arte","Cortina"]
print("Antes: ", p)

def porNoMay(e):
    return e.lower()

p.sort(key=porNoMay)

print("Despues: ", p)



