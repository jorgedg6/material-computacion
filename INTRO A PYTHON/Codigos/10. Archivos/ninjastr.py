r = open("ninjastr.txt")
ls = r.readlines()
r.close()

num = 0
for l in ls:
    if l == "BOB":
        num += 1
print("BOB ha aparecido",num,"veces")






