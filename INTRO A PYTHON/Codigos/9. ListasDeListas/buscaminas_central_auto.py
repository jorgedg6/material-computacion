# Asumir no esta en el borde
def minas(m,f,c):
    num = 0
    
    for i in range(-1,2):
        for j in range(-1,2):
            
            if m[f+i][c+j] == "X":
                num += 1
    return num
 


m = [["_","X","X","_"],
     ["_","_","_","_"],
     ["X","_","X","X"],
     ["_","_","X","X"],
     ["_","_","_","_"]]
     
r1 = minas(m,2,1)
print("F:",2,"C:",1,"Minas:",r1)

r2 = minas(m,1,2)
print("F:",1,"C:",2,"Minas:",r2)
