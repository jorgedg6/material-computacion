
r = open("header.txt")
ls = r.readlines()
r.close()

# Es una lista normal!
# El header es el elem 0 de la lista
# Toda la list des del elemento 1 hasta el final
ls2 = ls[1:]

suma = 0
for l in ls2:
    nota = float(l.strip())
    suma += nota

print("PROMEDIO",suma/len(ls2))

'''
r = open("header.txt")
ls = r.readlines()
r.close()

suma = 0
for l in ls:
    nota = float(l.strip())
    suma += nota

print("PROMEDIO",suma/len(ls))
'''








