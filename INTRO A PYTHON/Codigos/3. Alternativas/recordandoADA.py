'''
print("EMPEZAR PROGRAMA")

email = input("Email del estudiante? ")
hecho = input("Ha hecho la ADA 1? ")

if hecho == "NO":
    print("Enviando email a", email)

print("ACABAR PROGRAMA")
'''

'''
print("EMPEZAR PROGRAMA")

email = input("Email del estudiante? ")
hecho = input("Ha hecho la ADA 1? ")

if hecho == "NO" or hecho == "no" or hecho == "n" or hecho == "N":
    print("Enviando email a", email)

print("ACABAR PROGRAMA")
'''


print("EMPEZAR PROGRAMA")

email = input("Email del estudiante? ")
hecho = int(input("Ha hecho la ADA 1 (1-Si 2-No)? "))

if hecho == 2:
    print("Enviando email a", email)

print("ACABAR PROGRAMA")
