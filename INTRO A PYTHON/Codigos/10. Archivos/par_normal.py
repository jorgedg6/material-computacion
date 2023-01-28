import random

u = 0
c = 0

continuar = True
while continuar:
    op = int(input("1-Impar 2-Par 0-Salir? "))
    if op == 0:
        continuar = False
    else:
        du = int(input("Dedos (de 0 a 5)? "))
        dc = random.randint(0,5)
        suma = du + dc
        print(du,"+",dc,"=",suma)

        if (suma%2 == 0 and op == 2) or (suma%2 == 1 and op == 1):
            print("Punto USER")
            u += 1
        else:
            print("Punto COMP")
            c += 1

        print("USER",u,"COMP",c)



