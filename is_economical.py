def is_economical(n):
    Num = n
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
    listDigits = 0
    for key,value in listFctors.items():
        listDigits = listDigits + len(str(key))+len(str(value)) if value>1 else listDigits+len(str(key))
    if listDigits==len(str(Num)):
        return 'Equidigital'
    elif listDigits < len(str(Num)):
        return 'Frugal'
    elif listDigits > len(str(Num)):
        return 'Wasteful'


print(is_economical(14)) #"Equidigital"
print(is_economical(125)) #➞ "Frugal"
print(is_economical(1024)) #➞ "Frugal"
print(is_economical(30)) #➞ "Wasteful"
