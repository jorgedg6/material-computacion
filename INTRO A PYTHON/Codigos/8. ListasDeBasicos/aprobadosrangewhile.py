def num_aprobados_fr(notas):
    r = 0
    for i in range(0,len(notas)):
        if notas[i] >= 4.0:
            r += 1
    return r


n = [6.6, 2.3, 4.7, 3.3, 6.1]
a = num_aprobados(n)
print("Aprobados:",a) 







def num_aprobados_wh(notas):
    r = 0
    i = 0
    while i < len(notas):
        if notas[i] >= 4.0:
            r += 1
        i += 1
    return r


n = [6.6, 2.3, 4.7, 3.3, 6.1]
a = num_aprobados(n)
print("Aprobados:",a) 

