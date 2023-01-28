#Usando for in str
def contar(adn,b):
    num = 0
    for c in adn:
        if c == b:
            num += 1
    return num

#CODIGO PRINCIPAL
adn = input("ADN: ")

numA = contar(adn,"A")
numT = contar(adn,"T")
numG = contar(adn,"G")
numC = contar(adn,"C")

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




