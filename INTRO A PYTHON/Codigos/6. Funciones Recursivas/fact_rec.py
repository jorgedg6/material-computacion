def fact_rec(n):
    if n == 1:
        sol = 1
        return sol
    else:
        sol = n * fact_rec(n-1)
        return sol



x = fact_rec(1000)
print(x)


'''
y = fact_rec(4)
print(y)

z = fact_rec(5)
print(z)
'''


'''

def fact_rec2(n):
    if n == 1:
        sol = 1
    else:
        sol = n * fact_rec2(n-1)
    return sol



x = fact_rec2(3)
print(x)

y = fact_rec2(4)
print(y)

z = fact_rec2(5)
print(z)

'''


