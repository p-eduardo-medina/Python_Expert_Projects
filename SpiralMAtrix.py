def matrix(n):
    import numpy as np
    newMatrix = np.zeros((n,n))
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
        
            
            
        
        
 
 
 
print(matrix(3)== [[1, 2, 3], [8, 9, 4], [7, 6, 5]])
print(matrix(2)== [[1, 2], [4, 3]])
print(matrix(4)== [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
print(matrix(7)== [
    [1, 2, 3, 4, 5, 6, 7], 
    [24, 25, 26, 27, 28, 29, 8], 
    [23, 40, 41, 42, 43, 30, 9], 
    [22, 39, 48, 49, 44, 31, 10], 
    [21, 38, 47, 46, 45, 32, 11], 
    [20, 37, 36, 35, 34, 33, 12], 
    [19, 18, 17, 16, 15, 14, 13]])