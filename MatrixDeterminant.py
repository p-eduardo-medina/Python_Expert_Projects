#Create a function that returns the determinant of a given square matrix.
import numpy as np
def determinant(A):
    A = np.array(A)
    if A.shape == (1,1):  return A[0][0]
    elif A.shape == (2,2): return A[0][0]*A[1][1] - A[1][0]*A[0][1]
    else:
        det,sign = 0,1
        for index in range(len(A[0])):
            det += sign*A[0][index] * determinant( np.concatenate((A[1:,:index], A[1:,index+1:]), axis=1) )
            sign *= -1
    return det           
    
print(determinant([[1]]) ==1)
print(determinant([[-12]]) ==-12)
print(determinant([[1, 0], [5, 4]]) ==4)
print(determinant([[3, 0], [2, 2]]) ==6)
print(determinant([[0, 1], [4, 3]]) ==-4)
print(determinant([[27, 3], [50, 22]]) ==444)
print(determinant([[4, 8, 6],   [2, 4, 3], [6, 2, 1]]) ==0)
print(determinant([[4, 5, 4], [3, 1, 2], [3, 4, 3]]) ==1)
print(determinant([[8, 3, 6], [2, 1, 4], [9, 2, 3]]) ==20)
print(determinant([[7, 0, 6], [9, 8, 7], [6, 9, 7]]) ==149)
print(determinant([[3, 7, 0], [6, 0, 0], [1, 2, 8]]) ==-336)
print(determinant([[0, 4, 1, 1], [5, 5, 4, 1], [0, 0, 2, 0], [4, 2, 5, 0]]) ==12)
print(determinant([[5, 5, 2, 1], [3, 3, 0, 1], [3, 2, 1, 2], [0, 3, 0, 0]]) ==-24)
print(determinant([[4, -2, 3, -4], [5, 4, -1, -4], [0, -1, -3, 5], [0, -4, -1, 5]]) ==-19)
print(determinant([[16, 19, 13, -7], [1, 2, 10, 2], [8, 7, -16, -4], [-14, -19, 1, -3]]) ==-3720)
print(determinant([[3, 13, 6, 2], [-18, -20, 10, -8], [-11, -19, 6, 10], [-6, -14, -2, -13]]) ==-10292)
print(determinant([[-6, 0, 0, 6, 0, 0, -2], [5, 0, 0, 8, 0, 0, 0], [1, 2, -7, 6, 0, 0, 0], [0, 0, 0, 0, 9, 0, 2], [0, 3, -5, 0, 0, 0, 9], [0, 1, 0, 9, 0, -8, 0], [0, 0, 0, -10, 0, 0, 0]]) ==79200)
print(determinant([[-10, -2, -7, -3, 8, -9, 1], [8, -9, -8, 10, -5, -1, 7], [0, 5, 8, -2, -4, -10, 1], [1, -4, -10, -1, -2, 5, 8], [2, 7, 4, -7, 4, 4, -2], [5, -3, 5, -4, -7, -6, -3], [7, 7, -1, -4, 8, 4, 0]]) ==3032480)