def minas(m,f,c):

    nf = len(m)
    #Num cols son los elems de cualquier fila
    #por ejemplo la 0
    nc = len(m[0])
    
    num = 0
    
    for i in range(-1,2):
        for j in range(-1,2):

            fdentro = (f+i >= 0 and f+i < nf)
            cdentro = (c+j >= 0 and c+j < nc)

            if fdentro and cdentro:
                if m[f+i][c+j] == "X":
                    num += 1
    return num
 


m = [["_","X","X","_"],
     ["_","_","_","_"],
     ["X","_","X","X"],
     ["_","_","X","X"],
     ["_","_","_","_"]]

r0 = minas(m,0,1)
print("F:",0,"C:",1,"Minas:",r0)
     
r1 = minas(m,2,1)
print("F:",2,"C:",1,"Minas:",r1)

r2 = minas(m,1,2)
print("F:",1,"C:",2,"Minas:",r2)

r3 = minas(m,4,2)
print("F:",4,"C:",2,"Minas:",r3)
