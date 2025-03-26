def truncatable(n): 
    leftResult, rightResult = True, True
    for count in range(2):
        nStr = str(n)
        if '0'in nStr: return False

        if count==1: nStr= nStr[::-1]

        listTruncate = []
        for i in range(len(nStr)):
            if count==1:            
                listTruncate.append(nStr[i:len(nStr)][::-1])
            else:
                listTruncate.append(nStr[i:len(nStr)])
        #print(listTruncate)
        resultTruncate = True
        for num in listTruncate:
            result = findFactors(int(num))
            resultTruncate = resultTruncate and result
        if count == 0:
            leftResult = resultTruncate
        elif count == 1:
            rightResult = resultTruncate
    
    if leftResult and rightResult:
        return 'both'
    elif leftResult:
        return 'left'
    elif rightResult:
        return 'right'
    else:
        return False 
                
      
def findFactors(n) -> dict:
    #Find the factors
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
    #print(listFctors)
    newList = list(listFctors.values())    
    
    
    if (not bool(listFctors)): return False
    if len(newList)==1: 
        if newList[0]==1: return True
    else: return False


print(truncatable(47), "left")
print(truncatable(79), "right")
print(truncatable(349), False)
