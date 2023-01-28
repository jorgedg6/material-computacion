#Nombre, Interrog, Tareas
a = ["Alice"  ,6.5,5.5]
b = ["Bob"    ,4.3,5.9]
c = ["Charlie",1.3,6.1]
ns = [a,b,c]

#1- Definir la funcion para key
def porInt(e):
    return e[1]

#2- Ordenar usando la key
ns.sort(key=porInt)

print("0->",ns[0])
print("1->",ns[1])
print("2->",ns[2])






#Nombre, Interrog, Tareas
a = ["Alice"  ,6.5,5.5]
b = ["Bob"    ,4.3,5.9]
c = ["Charlie",1.3,6.1]
ns = [a,b,c]

#1- Definir la funcion para key
def porTareas(e):
    return e[2]

#2- Ordenar usando la key
ns.sort(key=porTareas)

print("0->",ns[0])
print("1->",ns[1])
print("2->",ns[2])






#Nombre, Interrog, Tareas
a = ["Alice"  ,6.5,5.5]
b = ["Bob"    ,4.3,5.9]
c = ["Charlie",1.3,6.1]
ns = [a,b,c]

#1- Definir la funcion para key
def porPromedio(e):
    promedio = e[1]+e[2]/2
    return promedio

#2- Ordenar usando la key
ns.sort(key=porPromedio)

print("0->",ns[0])
print("1->",ns[1])
print("2->",ns[2])
