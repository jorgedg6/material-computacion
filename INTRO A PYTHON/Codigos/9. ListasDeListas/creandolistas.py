#Crear lista de nombres (list de str)
nombres = []

num = int(input("Cuantos nombres? "))
for i in range(0,num):
    
    nombre = input("Nombre? ")
    nombres.append(nombre)

print(nombres)


#Crear lista de nombres (list de listas [str,float])
estudiantes = []

num = int(input("Numero estudiantes? "))
for i in range(0,num):

    nombre = input("Nombre? ")
    nota = float(input("Nota? "))

    est = [nombre,nota]
    estudiantes.append(est)

print(estudiantes)



           



        

