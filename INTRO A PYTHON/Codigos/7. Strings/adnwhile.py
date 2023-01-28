#Usando While
def contar_w(adn,b):
    num = 0
    i = 0
    while i < len(adn):
        c = adn[i]
        if c == b:
            num += 1
        i += 1
    return num

#CODIGO PRINCIPAL
adn = input("ADN: ")

numA = contar_w(adn,"A")
numT = contar_w(adn,"T")
numG = contar_w(adn,"G")
numC = contar_w(adn,"C")

print("Hay",numA, "As", numT, "Ts", numG, "Gs", numC, "Cs")


'''
#Entrada
adn = input("ADN: ")

#Para cada letra mirar si es igual A
numA = 0
for c in adn:
    if c == "A":
        numA += 1

#Para cada letra mirar si es igual T
numT = 0
for c in adn:
    if c == "T":
        numT += 1

#Para cada letra mirar si es igual G
numG = 0
for c in adn:
    if c == "G":
        numG += 1

#Para cada letra mirar si es igual C
numC = 0
for c in adn:
    if c == "C":
        numC += 1


#Salida
print("Hay",numA, "As", numT, "Ts", numG, "Gs", numC, "Cs")
'''




