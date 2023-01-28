s = "hola mundo!"

#Contiene el str
a = "m" in s
print(a)

#No contiene el str
b = "j" in s
print(b)

#Cualquier str (no solo letras)
c = "!" in s
print(c)

#Mayusculas y Minusculas son diferentes
d = "M" in s
print(d)

# Funciona para muchas de una letra
e = "mun" in s
print(e)

# Es un str (puede tener espacios, etc)
f = "la mu" in s
print(f)

#Se usa como cualquier bool
g = not ("j" in s)
print(g)



