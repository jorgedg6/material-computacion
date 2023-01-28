r = open("ninjastr.txt")
ls = r.readlines()
r.close()

num = 0
for l in ls:
    lx = l.strip() # 'lx' es 'l' pero sin el \n
    if lx == "BOB":
        num += 1
print("BOB ha aparecido",num,"veces")






