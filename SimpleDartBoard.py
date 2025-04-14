""" Create a function which creates a square
dartboard of side length n. The value of a 
number should increase, the closer it is to 
the centre of the board."""
def make_dartboard(n):
    import numpy as np
    import math
    Matrix = np.zeros(shape=[n,n], dtype=np.int32)
    HorStrt, VertStrt = 0,0
    HorLimit, VertLimit = n-1,n-1
    i,j,num,count = 0,0,math.ceil(n/2),0
    while True:
        if not count < n*n: break
        else: count+=1
        Matrix[i][j] = num
        if i == VertStrt:
            if j == HorLimit:
                i+=1
            else: j+=1
        elif j == HorLimit:
            if i == VertLimit:
                j -=1
            else: i+=1
        elif i == VertLimit:
            if j == HorStrt:
                i-=1
            else: j-=1
        elif j == HorStrt:
            if i == VertStrt+1:
                num         -= 1
                HorStrt     += 1
                VertStrt    += 1 
                HorLimit    -= 1
                VertLimit   -= 1
                j+=1
            else: 
                i-=1
    return Matrix
        

                
        
     
        


print(make_dartboard(3), [
	111,
	121,
	111
])

print(make_dartboard(8), [
	11111111,
	12222221,
	12333321,
	12344321,
	12344321,
	12333321,
	12222221,
	11111111
])

print(make_dartboard(5), [
	11111,
	12221,
	12321,
	12221,
	11111
])

print(make_dartboard(2), [
	11,
	11,
])

print(make_dartboard(1), [
	1
])

print(make_dartboard(4), [
	1111,
	1221,
	1221,
	1111
])

print(make_dartboard(6), [
	111111,
	122221,
	123321,
	123321,
	122221,
	111111
])

print(make_dartboard(7), [
	1111111,
	1222221,
	1233321,
	1234321,
	1233321,
	1222221,
	1111111
])

print(make_dartboard(9), [
	111111111,
	122222221,
	123333321,
	123444321,
	123454321,
	123444321,
	123333321,
	122222221,
	111111111
])

print(make_dartboard(23))