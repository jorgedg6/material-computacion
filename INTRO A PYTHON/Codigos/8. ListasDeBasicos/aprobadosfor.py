def num_aprobados(notas):
    r = 0
    for e in notas:
        if e >= 4.0:
            r += 1
    return r


n = [6.6, 2.3, 4.7, 3.3, 6.1]
a = num_aprobados(n)
print("Aprobados:",a) 









