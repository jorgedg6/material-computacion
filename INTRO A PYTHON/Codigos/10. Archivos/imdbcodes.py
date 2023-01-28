r = open("imdbsucio.txt")
ls = r.readlines()
r.close()

codes = []
for l in ls:
    cs = l.strip().split("/")
    for c in cs:
        if c[0:2] == "tt":
            codes.append(c[2:])

e = open("imdblimpio.txt","w")
for code in codes:
    print(code,file=e)
e.close()
    








