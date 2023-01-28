'''
tipo = input("cuadrado o rectangulo? ")

if tipo == "cuadrado":
    l = int(input("Lado? "))
    a = l*l
    print("Area:",a)
elif tipo == "rectangulo":
    b = int(input("Base? "))
    h = int(input("Altura? "))
    a = b*h
    print("Area:",a)
else:
    print("Opcion erronea")
'''


tipo = input("cuadrado o rectangulo? ")

if tipo == "cuadrado":
    l = int(input("Lado? "))
    a = l*l
elif tipo == "rectangulo":
    b = input("Base? ")
    h = input("Altura? ")
    a = b*h
else:
    print("Opcion erronea")

print("Area:",a)






           
