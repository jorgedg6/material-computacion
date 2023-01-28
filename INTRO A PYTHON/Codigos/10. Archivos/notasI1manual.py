'''

nest = int(input("Num de Estudiantes? "))

suma = 0
for i in range(0,nest):
    nota = float(input("Nota? "))
    suma += nota

print("Promedio:",suma/nest)
'''


ntotal = int(input("Num de Estudiantes? "))

nest = 0
suma = 0
for i in range(0,ntotal):
    nota = float(input("Nota? "))
    if nota != 1.0:
        nest += 1
        suma += nota

print("Promedio:",suma/nest)



