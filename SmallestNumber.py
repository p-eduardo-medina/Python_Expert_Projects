# Given a positive integer n, 
# implement a function that finds 
# the smallest number that is evenly 
# divisible by the integers 1 through n inclusive.
def smallest(n):
    nums = [n-i for i in range(n)]
    dictFactors = dict()
    for num in nums:
        numFactors = factors(num)
        for factor, power in numFactors.items():
            if factor in dictFactors.keys():
                if power>dictFactors[factor]: dictFactors[factor]=power
            else: dictFactors[factor] = power
    solution = 1
    for factor, power in dictFactors.items(): solution *= factor**power
    return solution
                    
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

    
print(smallest(1)   ==   1)
print(smallest(10)  ==   2520)
print(smallest(17)  ==   12252240)
print(smallest(31)  ==   72201776446800)
print(smallest(99)  ==   69720375229712477164533808935312303556800)
print(smallest(100) ==   69720375229712477164533808935312303556800)
print(smallest(101) ==   7041757898200960193617914702466542659236800)