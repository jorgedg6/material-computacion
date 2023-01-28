print("Bienvenidos a AEROMATIC")

i = 0
continuar = True

while continuar:
    print("CUADRADO", i)
    l = int(input("Lado? "))

    if l == -1:
        continuar = False
    else:
        a = l*l
        print("Area", a)
        i += 1

print("Gracias por usar AEROMATIC")


