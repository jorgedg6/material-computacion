
#CAJA HIMALAYA 10% descuento,
#CAJA TEIDE 5% descuento
#No acomulables
total = int(input("Total de la compra: "))
cajaT = input("Eres CAJA TEIDE: ")
cajaH = input("Eres CAJA HIMALAYA: ")


if cajaT == "si":
    total = total - (total*0.05)
elif cajaH == "si":
    total = total - (total*0.10)

print(total)


'''
#Isapre 20% descuento, Caja 10% descuento
#Los descuentos se pueden acomular
total = int(input("Total de la compra: "))
isapre = input("Eres ISAPRE CRUZNEGRA: ")
caja = input("Eres CAJA HIMALAYA: ")

if isapre == "si":
    total = total - (total*0.20)
elif caja == "si":
    total = total - (total*0.10)

print(total)
'''

'''
#Isapre 20% descuento, Caja 10% descuento
#Los descuentos se pueden acomular
total = int(input("Total de la compra: "))
isapre = input("Eres ISAPRE CRUZNEGRA: ")
caja = input("Eres CAJA HIMALAYA: ")

if caja == "si":
    total = total - (total*0.10)
elif isapre == "si":
    total = total - (total*0.20)
elif isapre == "si" and caja == "si":
    total = total - (total*0.30)

print(total)
'''    

'''
#Isapre 20% descuento, Caja 10% descuento
#Los descuentos se pueden acomular
total = int(input("Total de la compra: "))
isapre = input("Eres ISAPRE CRUZNEGRA: ")
caja = input("Eres CAJA HIMALAYA: ")

if isapre == "si" and caja == "si":
    total = total - (total*0.30)
elif caja == "si":
    total = total - (total*0.10)
elif isapre == "si":
    total = total - (total*0.20)

print(total)
'''


#Isapre 20% descuento, Caja 10% descuento
#Los descuentos se pueden acomular
total = int(input("Total de la compra: "))
isapre = input("Eres ISAPRE CRUZNEGRA: ")
caja = input("Eres CAJA HIMALAYA: ")

if isapre == "si" and caja == "si":
    total = total - (total*0.30)
    
if caja == "si":
    total = total - (total*0.10)
    
if isapre == "si":
    total = total - (total*0.20)

print(total)
