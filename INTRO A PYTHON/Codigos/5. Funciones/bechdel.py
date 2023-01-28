def bechdel(m):
    print("En la pelicula",m," ...")
    pasa = regla1()
    if pasa:
        pasa = regla2()
    if pasa:
        pasa = regla3()
    return pasa

def regla1():
    op = int(input("... aparecen al menos dos mujeres con nombre? (1-Si 2-No) "))
    res = op == 1
    return res

def regla2():
    op = int(input("... hablan entre si? (1-Si 2-No) "))
    res = op == 1
    return res

def regla3():
    op = int(input("... hablan de otra cosa que no sea un hombre? (1-Si 2-No) "))
    res = op == 1
    return res
    

# CODIGO PRINCIPAL
p = input("Pelicula? ")
r = bechdel(p)
if r:
    print(p,"pasa el Bechdel Test")
else:
    print(p,"NO pasa el Bechdel Test")

