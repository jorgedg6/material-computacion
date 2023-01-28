def apneas(s):
    num = 0
    for i in range(0,len(s)-1):
        if s[i:i+2] == ".X":
            num += 1
    return num


def max_apnea(s):
    maxi = 0
    l = 0
    for i in range(0,len(s)):
        if s[i] == "X":
            l += 1
        elif s[i] == ".":
            if l > maxi:
                maxi = l
            l = 0
    return maxi


def kventana(s,k):
    res = False
    for i in range(0,len(s)-k+1):
        v = s[i:i+k]
        num = 0
        for c in v:
            if c == "X":
                num += 1
        if num > len(v) / 2:
            res = True
    return res
        
    


    

#CODIGO PRINCIPAL (TEST)
s1 = "...XXX...X.X....XXXX......X.XXX.........XXX....XX..X."
print("==S1==")
print(apneas(s1))
print(max_apnea(s1))
print(kventana(s1,5))
print(kventana(s1,8))


s2 = "...XXX....X...XXXX...XXXX....XXX....XX..XXXXX."
print("==S2==")
print(apneas(s2))
print(max_apnea(s2))
print(kventana(s2,5))
print(kventana(s2,8))
      
    
s3 = ".........................."
print("==S3==")
print(apneas(s3))
print(max_apnea(s3))
print(kventana(s3,5))
print(kventana(s3,8))

s4 = ".XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX."
print("==S4==")
print(apneas(s4))
print(max_apnea(s4))
print(kventana(s4,5))
print(kventana(s4,8))

s5 = ".X...............XX................XX.............X......"
print("==S5==")
print(apneas(s5))
print(max_apnea(s5))
print(kventana(s5,5))
print(kventana(s5,8))
