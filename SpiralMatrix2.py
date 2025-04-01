def matrix(n,m):
    import numpy as np
    newMatrix = np.zeros((n,m))
    index,i,j = 0,0,0
    iInit,iLimit = 0,newMatrix.shape[0]-1
    jInit,jLimit = 0,newMatrix.shape[1]-1
    while index < newMatrix.shape[0]*newMatrix.shape[1]:
        if (i == iInit) :
            newMatrix[i][j] = index+1
            if j == jLimit:
                i+=1
            else: j+=1
        elif j==jLimit:
            newMatrix[i][j] = index+1
            if i == iLimit:
                j-=1
            else: i+=1
        elif i == iLimit:
            newMatrix[i][j] = index+1
            if j == jInit:
                i-=1
            else: j-=1
        elif j == jInit:
            newMatrix[i][j] = index+1
            if i == iInit+1:
                j+=1
                iInit+=1
                jInit+=1
                iLimit-=1
                jLimit-=1
            else: i-=1
        else: print("Something's Wrong")
        index+=1
    listMatrix = []
    for i in range(newMatrix.shape[0]):
        subList = []
        for j in range(newMatrix.shape[1]):
            subList.append(int(newMatrix[i][j]))
        listMatrix.append(subList)
    return listMatrix


mat = matrix(8,3)
for row in mat:
    print(row)