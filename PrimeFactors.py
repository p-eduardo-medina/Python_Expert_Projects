def factors(n):
    listFctors = {}
    i = 2
    while i*i<=n:
        if n%i==0:
            n/=i
            if i in listFctors.keys():
                listFctors[int(i)]+=1
            else:
                listFctors[int(i)]=1
        else:
            i+=1
    if n>1:
        if int(n) in listFctors.keys():
                listFctors[int(n)]+=1
        else:
            listFctors[int(n)]=1
    return listFctors