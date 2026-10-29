def crack_pincode(pincode):
    import itertools
    numberLayout = [
        [1 ,2, 3],
        [4 ,5, 6],
        [7 ,8, 9],
        ["",0, ""]
        ]
    indexBase = []
    for num in pincode:
        indexBase.append([[i,j] 
                    for i in range(len(numberLayout)) 
                    for j in range(len(numberLayout[0])) 
                    if int(num) == numberLayout[i][j]
                    ][0])
    output = []
    posibilities = []
    for index in indexBase:
        pos = []
        for i in range(-1,2):
            for j in range(-1,2):
                if index[0] + i >=0 and index[0] + i  <4 and index[1] + j>=0 and index[1] + j < 3 and ((j==0)^(i==0)):
                    if isinstance(numberLayout[ index[0] + i ][index[1] + j] ,int):
                        pos.append(numberLayout[ index[0] + i ][index[1] + j])
        posibilities.append(pos)
    posibilities = [[int(pincode[index])]+posibilities[index] for index in range(len(pincode))]
    posibilities = ["".join(str(num) for num in my_tuple) for my_tuple in list(itertools.product(*posibilities))]
    return sorted(posibilities, key=int)

def crack_pincode2(c):
	d,L="08,124,1235,236,1457,24568,3569,478,05789,689".split(','),[""]
	for p in c: L = [y+x for y in L for x in d[int(p)]]
	return L


print(crack_pincode("0"))
print(crack_pincode("2"))
print(crack_pincode("46"))
print(crack_pincode2("007"))
