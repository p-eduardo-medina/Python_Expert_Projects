def lcm(nums):
    listFactors = {}
    for n in nums:
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
        for key, value in listFctors.items():
            if key in listFactors.keys():
                if listFctors[key]>listFactors[key]:
                    listFactors[key] = listFctors[key]
            else:
                listFactors[key] = listFctors[key]
    lcm = 1
    for number,power in listFactors.items():
        lcm*=number**power
           
    return lcm

print(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) )# 2520

print(lcm([5])) # 5

print(lcm([5, 7, 11])) #385

print(lcm([5, 7, 11, 35, 55, 77])) # 385
print(lcm([5, 7, 11, 35, 55, 77])) # 385
