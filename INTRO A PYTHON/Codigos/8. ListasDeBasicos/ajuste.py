vs = []

n = int(input("Numero de estudiantes? "))

#Pedir y recopilar los votos
for i in range(0,n):
    print("Estudiante",i)
    v = int(input("Ajuste 1-Si 2-No? "))
    vs.append(v)

#Contar los votos
numsi = 0
numno = 0
for e in vs:
    if e == 1:
        numsi += 1
    elif e == 2:
        numno += 1

#Se imprime el resultado
print("SI:",numsi,"NO:",numno)
if numsi > numno:
    print("SE APRUEBA")
elif numsi < numno:
    print("SE RECHAZA")
else:
    print("EMPATE")






