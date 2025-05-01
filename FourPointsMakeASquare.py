# The function is given four points with (x, y) coordinates in no particular order.
# Determine if these points make a square and return True / False.
# A square has four equal sides with positive length and four 90-degree angles.
import numpy as np
def valid_square(p1, p2, p3, p4):
    Points = [p1,p2,p3,p4]
    for point in Points: 
        Directions = [ [point[0]-finalPoint[0],point[1]-finalPoint[1]] for finalPoint in Points if finalPoint!=point]
        Angles = [ dotProduct( Directions[0], direction )*180/np.pi for direction in Directions if direction!=Directions[0] ]
        if not (any(angle == 90 for angle in Angles) or sum(Angles)==90): return False
    return True

def dotProduct(v1,v2): return np.arccos(  ( v1[0]*v2[0] + v1[1]*v2[1] ) / ( np.sqrt(v1[0]**2 + v1[1]**2) * np.sqrt(v2[0]**2 + v2[1]**2) )  )


from time import perf_counter
tic = perf_counter()
print(valid_square((0, 0), (1, 1), (1, 0), (0, 1)) == True)
print(valid_square((0, 0), (1, 1), (1, 0), (0, 12)) == False)
print(valid_square((1, 0), (-1, 0), (0, 1), (0, -1)) == True)
print(valid_square((0, 0), (0, 0), (0, 0), (0, 0)) == False)
print(valid_square((0, 4), (4, 6), (3, 3), (1, 7)) == True)
print(valid_square((11, 23), (16, 32), (18, 18), (23, 25)) == False)
print(valid_square((2, 2), (8, 15), (-11, 8), (-5, 21)) == True)
print(valid_square((-16, 20), (-18, 3), (-1, -1), (3, 16)) == False)
print(valid_square((-28, 16), (-27, 11), (-22, 17), (-21, 11)) == False)
print(valid_square((41, -37), (49, 10), (2, 18), (-6, -29)) == True)
print(valid_square((-74, 89), (-28, 71), (-46, 25), (-92, 43)) == True)
print(valid_square((23, 36), (1, -36), (45, -14), (-21, 8)) == False)
print(valid_square((-29, 88), (-43, 19), (-112, 33), (-98, 102)) == True)
print(valid_square((15, 125), (-86, 133), (-31, 179), (-41, 78)) == False)
print(valid_square((-149, 115), (-28, 158), (-110, 197), (-67, 76)) == True)
print(valid_square((148, 349), (169, 96), (32, 212), (285, 233)) == True)
print(valid_square((-84, 19), (56, -48), (-2, -187), (-141, -130)) == False)
print(valid_square((77, -133), (42, 164), (207, 34), (-91, -3)) == False)
print(valid_square((-922, 84), (-1088, 1061), (55, 250), (-111, 1227)) == True)
print(valid_square((53, 2547), (22, 787), (919, 1650), (-840, 1681)) == False)
print(valid_square((-1040, 1021), (-1069, 729), (-748, 992), (-777, 700)) == True)

print('t_sec = {:.6f}'.format(perf_counter() - tic))