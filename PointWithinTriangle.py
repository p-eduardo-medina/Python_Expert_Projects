from itertools import permutations
def within_triangle(p1, p2, p3, test):
    list_ofPermutations = list(permutations([p1, p2, p3]))
    list_of_Points = [ n for n in list_ofPermutations if list_ofPermutations.index(n)%2==1 ]
    print(list_of_Points)
    for coord in list_of_Points:
        try:
            m1 = (coord[0][1]-coord[1][1])/(coord[0][0]-coord[1][0])
            m2 = (coord[0][1]-coord[2][1])/(coord[0][0]-coord[2][0])
            mt = (test[1]-coord[0][1])/(test[0]-coord[0][0])
            if mt > max(m1, m2) or mt < min(m1, m2): return False
        except ZeroDivisionError:
            continue
    return True





print(within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) == True)
print(within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) == False)
print(within_triangle((1, 7), (2, 4), (9, 3), (2, 6)) == True)
print(within_triangle((1, 7), (2, 4), (9, 3), (6, 5)) == False)
print(within_triangle((-2, 6), (12, -3), (1, 7), (9, -1)) == True)
print(within_triangle((-2, 6), (12, -3), (1, 7), (4, 2)) == False)
print(within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) == True)
print(within_triangle((-6, 2), (-2, -2), (8, 4), (0, -4)) == False)
