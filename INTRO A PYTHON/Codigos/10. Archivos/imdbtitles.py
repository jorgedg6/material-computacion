r = open("IMDBtitles.txt")
ls = r.readlines()
r.close()

p = input("Palabra? ")
num = 0
for l in ls:
    peli = l.strip()
    if p.lower() in peli.lower():
        num += 1

print(num,"veces")









