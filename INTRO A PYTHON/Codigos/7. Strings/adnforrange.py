#Usando for in range
def contar_fr(adn,b):
    num = 0
    for i in range(0,len(adn)):
        c = adn[i]
        if c == b:
            num += 1
    return num

#CODIGO PRINCIPAL
adn = input("ADN: ")

numA = contar_fr(adn,"A")
numT = contar_fr(adn,"T")
numG = contar_fr(adn,"G")
numC = contar_fr(adn,"C")

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




