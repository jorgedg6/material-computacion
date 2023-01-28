#Entrada
adn = input("ADN: ")
b = input("Base (A,T,G,C): ")

#Para cada letra mirar si es igual
num = 0
for c in adn:
    if c == b:
        num += 1

#Salida
print("El numero de", b, "es", num)





