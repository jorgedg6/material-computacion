largo = input("Email: ")

#Buscar la arroba (siempre hay)
for i in range(0,len(largo)):
    if largo[i] == "@":
        a = i

#Quedarse con el user
user = largo[:a]

#Quitar puntos
sp = ""
for c in user:
    if c != ".":
        sp = sp + c

#Mirar si hay +
#(pos si hay, o -1 si no hay)
m = -1
for i in range(0,len(sp)):
    if sp[i] == "+":
        m = i

#Quitar despues de +
if m != -1:
    limpio = sp[:m]
else:
    limpio = sp

#Minuscula
limpiomin = limpio.lower()

#Agregar el gmail
final = limpiomin+"@gmail.com"
print(final)









