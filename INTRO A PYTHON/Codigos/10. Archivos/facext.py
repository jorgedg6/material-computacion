fr = open("Facultades.csv")
fls = fr.readlines()
fr.close()

rr = open("Red.csv")
rls = rr.readlines()
rr.close()


#Header
e = open("Extendido.csv","w")
header = rls[0].strip()+",Facultad"
print(header,file=e)

for l in rls[1:]:
    cs = l.strip().split(",")

    #Buscar facultad
    for f in fls[1:]:
        fcs = f.strip().split(",")
        if fcs[0] == cs[4]:
            fac = fcs[1]

    #Imprimir (lo hariamos asi)
    #print(cs[0],cs[1],cs[2],cs[3],cs[4],cs[5],fac)
    #Uffff y si en vez de 7 son 70 ufffff

    #Si tienes una list de STR puedes crear un str
    #juntando los elementos con un str entre ellos
    s = ",".join(cs)
    s = s + ","+fac
    print(s,file=e)
    
e.close()


