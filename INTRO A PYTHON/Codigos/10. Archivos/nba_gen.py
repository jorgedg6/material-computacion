import random

ps = ["Barkley","Bird","Ewing","Johnson","Jordan","Malone","Pippen","Stockton"]

cs = []
for i1 in range(0,4): 
    for i2 in range(i1+1,5):
        for i3 in range(i2+1,6):
            for i4 in range(i3+1,7):
                for i5 in range(i4+1,8):
                    c = [ps[i1],ps[i2],ps[i3],ps[i4],ps[i5]]
                    cs.append(c)
random.shuffle(cs)

e = open("nba.csv","w")
for c in cs:
    print(c[0],c[1],c[2],c[3],c[4],sep=";",file=e)
    n0 = random.randint(0,6)
    n1 = random.randint(0,6)
    n2 = random.randint(0,6)
    n3 = random.randint(0,6)
    n4 = random.randint(0,6)
    print(n0,n1,n2,n3,n4,sep=";",file=e)
e.close()
