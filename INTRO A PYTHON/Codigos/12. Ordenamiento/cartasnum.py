def porAscDes(e):
    n1 = e[0]
    n2 = e[1]

    # Para n2 quiero que 12 antes de 4
    # Como mayor es el n2 mas pequeno lo quiero
    # Pues lo convierto en negativo
    # (multiplicandolo por -1)
    # -12 es mas pequeno que -4
    nn2 = n2 * -1
    
    return n1, nn2

def ordenar_cartas(b):
    b.sort(key=porAscDes)


#TEST
b = [[8,2],[9,3],[1,4],[8,1],
     [2,2],[5,1],[1,1],[7,3]]

print("Des:", b)
ordenar_cartas(b)
print("Ord:", b)



