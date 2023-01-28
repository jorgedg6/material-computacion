import random

#Auto-Load partida
r = open("parsave.txt")
ls = r.readlines()
r.close()

u = int(ls[0].strip())
c = int(ls[1].strip())

continuar = True
while continuar:
    op = int(input("1-Impar 2-Par 0-Salir? "))
    if op == 0:
        continuar = False

        #Auto-save
        #Creo otra vez el archivo en el formato de siempre
        e = open("parsave.txt","w")
        print(u,file=e)
        print(c,file=e)
        e.close()
        
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

