r = open("ninjaint.txt")
ls = r.readlines()
r.close()

num = 0
for l in ls:
    n = int(l)
    if n == 777:
        num += 1
print("777 ha aparecido",num,"veces")






