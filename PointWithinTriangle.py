def within_triangle(p1, p2, p3, test):
  def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
  d1 = sign(test, p1, p2)
  d2 = sign(test, p2, p3)
  d3 = sign(test, p3, p1)
  fl_neg = (d1 < 0) and (d2 < 0) and (d3 < 0)
  fl_pos = (d1 > 0) and (d2 > 0) and (d3 > 0)
  return fl_neg or fl_pos





print(within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) == True)
print(within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) == False)
print(within_triangle((1, 7), (2, 4), (9, 3), (2, 6)) == True)
print(within_triangle((1, 7), (2, 4), (9, 3), (6, 5)) == False)
print(within_triangle((-2, 6), (12, -3), (1, 7), (9, -1)) == True)
print(within_triangle((-2, 6), (12, -3), (1, 7), (4, 2)) == False)
print(within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) == True)
print(within_triangle((-6, 2), (-2, -2), (8, 4), (0, -4)) == False)
