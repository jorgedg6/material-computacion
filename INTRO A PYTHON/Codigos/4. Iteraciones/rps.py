import random

vu = 0
vc = 0
i = 0

#Hasta que uno llegue a 3 victorias
while vu < 3 and vc < 3:
    print("PARTIDA",i)

    continuar = True
    while continuar: #Continuar hasta que no empaten
        u = int(input("0->Rock, 1->Paper, 2->Scissors: "))
        c = random.randint(0,2)

        if u == c:
            print("Empate",u,c)
        elif(u == 0 and c == 1) or (u == 1 and c == 2) or (u == 2 and c == 0): 
            print("Victoria COMP", u,c)
            vc += 1
            continuar = False
        elif (u == 1 and c == 0) or (u == 2 and c == 1) or (u == 0 and c == 2):
            print("Victoria USER",u,c)
            vu += 1
            continuar = False
    i+=1
    
if vu == 3:
    print("USER GANA")
elif vc == 3:
    print("COMP GANA")


