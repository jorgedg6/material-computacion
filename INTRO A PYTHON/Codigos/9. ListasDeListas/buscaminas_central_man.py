# Asumir no esta en el borde
def minas(m,f,c):
    num = 0
    if m[f-1][c-1] == "X":
        num += 1
    if m[f-1][c] == "X":
        num += 1
    if m[f-1][c+1] == "X":
        num += 1
    if m[f][c-1] == "X":
        num += 1
    if m[f][c+1] == "X":
        num += 1
    if m[f+1][c-1] == "X":
        num += 1
    if m[f+1][c] == "X":
        num += 1
    if m[f+1][c+1] == "X":
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
