#Metodo sort - modifica lista original
p = [3, 1, 70, -1, 3, 7, 5]
print("Antes: ", p)
p.sort()
print("Despues: ", p)

#Metodo sort - modifica lista original
p = ["casa", "auto", "sillon", "silla"]
print("Antes: ", p)
p.sort()
print("Despues: ", p)

#May y Min son diferentes
p = ["Casa", "caracol", "Barco", "Arbol", "auto"]
print("Antes: ", p)
p.sort()
print("Despues: ", p)


#Ordenar descendentemente con sort y reverse
p = [3, 1, 70, -1, 3, 7, 5]
print("Antes: ", p)
p.sort()
p.reverse()
print("Despues: ", p)

#Ordenar descendentemente sin reverse
p = [3, 1, 70, -1, 3, 7, 5]
print("Antes: ", p)
p.sort()

#.... crear lista descendente manualmente
q = []
i = len(p)-1
while i >= 0:
    q.append(p[i])
    i = i - 1

print("Despues: ", q)


#Solo los 3 primeros
p = [13, 10, 5, 70, 8, 7, 3]
print("Antes: ", p)
p.sort()
q = p[0:3] #p es una lista normal y corriente!
print("Despues: ", q)


