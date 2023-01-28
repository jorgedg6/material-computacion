mi = "abcdefghijklmnopqrstuvwxyz"
ma = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"

t = input("Texto: ")

nmi = 0
nma = 0
nnum = 0
notr = 0

for c in t:
    if c in mi:
        nmi += 1
    elif c in ma:
        nma += 1
    elif c in num:
        nnum += 1
    else:
        notr += 1

print("MIN",nmi,"MAY",nma,"NUM",nnum,"OTROS",notr)



