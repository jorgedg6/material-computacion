import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

s1 = (b**2) - (4*a*c)
t1 = (-b) + math.sqrt(s1)
x1 = t1 / (2*a)

s2 = (b**2) - (4*a*c)
t2 = (-b) - math.sqrt(s2)
x2 = t2 / (2*a)

print("Las soluciones son", x1, "y", x2)



