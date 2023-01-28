def num_abiertas(cs,x):
    num = 0
    a = x
    encontrado = False

    while not encontrado:
        v = cs[a]
        num += 1
        if v == x:
            encontrado = True
        else:
            a = v

    return num



#TEST
cs = [3,2,5,4,6,1,0]
print("Prisionero",3,"Abiertas",num_abiertas(cs,3))
print("Prisionero",2,"Abiertas",num_abiertas(cs,2))



