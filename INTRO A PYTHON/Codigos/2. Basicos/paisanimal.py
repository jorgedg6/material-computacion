#Pedir el numero
numero = int(input("Piensa un numero del 2 al 10: "))

# Multiplicarlo por 9
print("Multiplica el numero por 9")
numero2 = numero * 9
print(numero, "* 9 =", numero2)

#Suma las dos cifras
print("Suma las dos cifras")
cifra1 = numero2 // 10
cifra2 = numero2 % 10
numero3 = cifra1 + cifra2
print(cifra1, "+", cifra2, "=", numero3)

# Resta 5
print("Resta 5")
numero4 = numero3 - 5
print(numero3, "- 5 =", numero4)

#Transforma el numero en letra
print("Transforma numero en letra: 1->A, 2->B, ...")
print(numero4, "-> D")

#Piensa pais con esa letra
print("Piensa un pais que empiece con esa letra")

#Piensa un animal con la segunda letra del pais
print("Piensa un animal que empiece con la 2a letra del pais")

#Leer mente
input("Listo para que te lea la mente?")
print("."*10)
print("."*10)
print("En DINAMARCA no hay IGUANAS!!!!")


