'''
monto = int(input("Cuanto necesitamos minimo? "))

llevamos = 0
while llevamos < monto:
    print("Le toca al siguiente!")
    m = int(input("¿Cuanto pones?: "))
    llevamos = llevamos + m
    print("Llevamos",llevamos)

print("¡Buena! Necesitando", monto, "conseguimos", llevamos)
'''    

'''
monto = int(input("Cuanto necesitamos minimo? "))

llevamos = 0
gente = 0
while llevamos < monto:
    print("Le toca a la Persona", gente)
    m = int(input("Cuanto pones? "))
    llevamos = llevamos + m
    gente = gente + 1
    print("Llevamos", llevamos)

print("Buena! Necesitabamos",monto,"y conseguimos",llevamos,"con",gente,"personas")
'''

'''
monto = int(input("Cuanto necesitamos minimo? "))
somos = int(input("Cuantos somos? "))

plata = 0
gente = 0

while plata < monto and gente < somos:
    print("Le toca a la Persona", gente)
    m = int(input("Cuanto pones? "))
    plata = plata + m
    gente = gente + 1
    print("Llevamos", plata, "de plata y", gente, "personas")

#Si acaba el while es que una de las dos condiciones es falsa
#O la plata ha superado el monto O la gente que puso ha superado a cuantos eramos

if plata >= monto:
    print("Buena! Necesitabamos",monto,"y conseguimos",plata,"con",gente,"personas")
else:
    print("No alcanzamos! Necesitabamos",monto,"y conseguimos",plata, "Sois unos tacanos!")
'''



monto = int(input("Cuanto necesitamos minimo? "))

llevamos = 0
continuar = True

while continuar:
    print("Le toca al siguiente!")
    m = int(input("¿Cuanto pones?: "))
    llevamos = llevamos + m
    print("Llevamos",llevamos)

    if llevamos >= monto:
        continuar = False

print("¡Buena! Necesitando", monto, "conseguimos", llevamos)


