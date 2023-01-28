r = open("nba.csv")
ls = r.readlines()
r.close()

#List de [n,s] con el nombre jugador
#y la suma de sus estrellas
ss = []
i = 0
while i < len(ls):
    pcs = ls[i].strip().split(";")
    ics = ls[i+1].strip().split(";")

    #Por cada jugador el quinteto
    for j in range(0,5): 
        nom = pcs[j]

        #Por cada jugador del quinteto que
        #no es el que estoy mirando
        for k in range(0,5):
            if j != k:
                star = int(ics[k])
            
                esta = False
                for s in ss:
                    if s[0] == nom:
                        s[1] += star
                        esta = True

                if not esta:
                    ss.append([nom,star])
    i+=2

#Maximo
maxn = -1
maxp = ""
for s in ss:
    if s[1] > maxn:
        maxp = s[0]
        maxn = s[1]
print(maxn,maxp)


