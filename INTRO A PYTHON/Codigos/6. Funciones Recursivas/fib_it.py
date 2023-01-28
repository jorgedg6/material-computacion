
def fib_it(n):
    if n == 1:
        s = 1

    elif n == 2:
        s = 1

    else:
        n1 = 1
        n2 = 1
        fib = n1+n2
        i = 3
        while i < n:
            n1 = n2
            n2 = fib
            fib = n1 + n2
            i += 1
        s = fib
        
    return s


x = fib_it(3)
print(x)

y = fib_it(4)
print(y)

z = fib_it(5)
print(z)


