
#Agregar al final
p = ["arbol","barco","casa","dado"]
p.append("estufa")
print(p)

#Sacar el elemento de la posicion tal
q = ["arbol","barco","casa","dado"]
q.pop(2)
print(q)

#Pop no solo lo saca, sino que lo retorna
#asi que lo podemos guardar en una variable
#si nos interesa
r = ["arbol","barco","casa","dado"]
x = r.pop(2)
print(x)
print(r)

#Si queremos agregar un elemento en una posicion concreta
#lo podemos hacer con slicing y concatenar
s = ["arbol","barco","dado","estufa"]
t = s[0:2]+["caracol"]+s[2:]
print(t)




