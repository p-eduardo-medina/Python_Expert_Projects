# The function is given four points with (x, y) coordinates in no particular order.
# Determine if these points make a square and return True / False.
# A square has four equal sides with positive length and four 90-degree angles.
def valid_square(p1, p2, p3, p4):
  if (p1==p2 or p1==p3 or p1==p4): return False
  distances = []
  for point in [p1,p2,p3,p4]:
     lst = [p1,p2,p3,p4]
     lst.remove(point)
     distance = [ (point[0]-p[0])**2+(point[1]-p[1])**2 for p in lst]
     distances.append([max(distance),min(distance)])
  if not all(d[0]==distances[0][0] and d[1]==distances[0][1] for d in distances):return False  
  return True  



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