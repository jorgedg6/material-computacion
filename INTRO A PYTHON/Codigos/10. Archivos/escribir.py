'''
ns = ["ALICE","BOB","CHARLIE","DAVID"]

for e in ns:
    print(e)
'''


ns = ["ALICE","BOB","CHARLIE","DAVID"]

#OPEN (con "w")
e = open("escribir.txt","w")

#PRINT
for n in ns:
    print(n,file=e)           

#CLOSE
e.close()
