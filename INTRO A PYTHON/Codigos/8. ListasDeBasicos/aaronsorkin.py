#'o' list de video original
#'ini' int del inicio del corte
#'fin' int del fin del corte
#'r' list de relleno 

def fake(o,ini,fin,r):
    first = o[:ini]
    last = o[fin+1:]
    m = first+r+last
    return m


#CODIGO DE TEST
a = ["Estoy","en","contra","del","confinamiento"]
i = 1
f = 2
r = ["a","favor"]
m = fake(a,i,f,r)

print(a)
print(m)

