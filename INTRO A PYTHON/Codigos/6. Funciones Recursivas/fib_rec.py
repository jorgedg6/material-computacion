
def fib_rec(n):
    
    #CASO BASE 1
    if n == 1:
        s = 1
    #CASO BASE 2:
    elif n == 2:
        s = 1
    #CASO RECURSIVO
    else:
        s = fib_rec(n-1)+fib_rec(n-2)

    return s

x = fib_rec(3)
print(x)

y = fib_rec(4)
print(y)

z = fib_rec(5)
print(z)


