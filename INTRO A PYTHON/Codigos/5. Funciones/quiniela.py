import random

lim1 = 50
lim2 = 80

for i in range(1,15):
    n = random.randint(1,100)
    if n < lim1:
        s = "1"
    elif n > lim2:
        s = "2"
    else:
        s = "X"

    print(i,"=>",s)

