# You're given a dartboard divided into sections,
# each section has a unique score.
# That means there won't be two sections with the same score.
import itertools
def darts_solver(sections, darts, target):
    lstSolution = []
    perm_set = []
    for i in range(1,darts+1):  perm_set+=list(itertools.combinations(sections,i))
    for Nums in perm_set:
        Nums = list(Nums)
        if len(Nums)!=darts:
            NumExtention = int(target/min(Nums))+1
            multiply_set = list( itertools.permutations( [i for i in range(1,NumExtention)] , len(Nums)) )
            for multiplyNum in multiply_set:
                suma = sum([x*y for x,y in zip(Nums,multiplyNum)]) 
                flag = False
                if suma==target and sum(multiplyNum) == darts:
                    strSolution = []
                    for i,num in enumerate(Nums):
                        strSolution += [num for j in range(multiplyNum[i])]
                    strSolution.sort()
                    if not strSolution in lstSolution: lstSolution.append(strSolution)
                    flag = True
                    break
                if flag: break
        else:
            if sum(Nums)==target:
                lstSolution.append(list(Nums))
    lstSolution = sorted(lstSolution,
                         key = lambda x:x[0])
    newList = []
    for lista in lstSolution:
        strSolution = ''
        for num in lista:
            strSolution+=str(num)+'-'
        newList.append(strSolution[:len(strSolution)-1])
    return newList


print(darts_solver([3, 6, 8, 11, 15, 19, 22], 3, 35)==["8-8-19"])
print(darts_solver([2, 4, 7, 10, 13, 18, 24], 3, 29)==["4-7-18"])
print(darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 40)==["11-11-18"])
print(darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 8)== [])
print(darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 32)== ["3-11-18", "7-7-18", "7-11-14"])
print(darts_solver([3, 7, 11, 14, 18, 20, 25, 29, 34],3, 67)==["18-20-29"])
print(darts_solver([3, 7, 11, 14, 18, 20, 25], 4, 23)==["3-3-3-14"])