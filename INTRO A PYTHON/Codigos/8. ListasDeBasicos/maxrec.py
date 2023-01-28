def max_rec(q):

    #CASO BASE
    if len(q) == 1:     #Un num
        return q[0]     #El max es el num

    #CASO RECURSIVO
    else:
        h = q[0]        #Primer num
        b = q[1:]       #Resto de nums

        mb = max_rec(b) #Et tu, dame el max del resto

        if h > mb:  
            res = h
        else:
            res = mb
        return res
    


a = [8,23,-1,7,30,6]
maxi = max_rec(a)
print(maxi)

    
    




