import random

r = open("idiomas.csv")
ls = r.readlines()
r.close()

#Que elija los idiomas
idiomas = ls[0].strip().split(";")
for i in range(0,len(idiomas)):
    print(i,"<-",idiomas[i])
de = int(input("De ...? "))
a = int(input("A ...? "))


continuar = True
while continuar:
    #Palabra al azar
    az = random.randint(1,len(ls)-1)
    cs = ls[az].strip().split(";")
    pde = cs[de]
    pa = cs[a]

    print(pde)
    res = input()

    if res == "EXIT":
        continuar = False
    elif res != pa:
        print("ERROR - ",pa)
    
        
    
    
    








