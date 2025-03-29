def overlapping_rectangles(rect1, rect2):
    #rect = [x, y, width, height].
    XA1, YA1, XA2, YA2 = rect1[0],rect1[1], rect1[0]+rect1[2], rect1[1]+rect1[3]
    XB1, YB1, XB2, YB2 = rect2[0],rect2[1], rect2[0]+rect2[2], rect2[1]+rect2[3]
    intRectX,intRectY = [],[]
    maxX,minX = max([XA1,XA2,XB1,XB2]), min([XA1,XA2,XB1,XB2])
    intRectX = [XA1,XA2,XB1,XB2]
    intRectX.remove(maxX)
    intRectX.remove(minX)
    maxY,minY = max([YA1,YA2,YB1,YB2]), min([YA1,YA2,YB1,YB2])
    intRectY = [YA1,YA2,YB1,YB2]
    intRectY.remove(maxY)
    intRectY.remove(minY)
    if ((rect1[0] + rect1[2]>rect2[0])and(rect1[1] + rect1[3]>rect2[1])):
        return (abs(intRectX[0]-intRectX[1]))*(abs(intRectY[0]-intRectY[1]))
    else:
        return 0
    
	
print(f'{overlapping_rectangles( [1, 1, 2, 2],[4, 4, 2, 2])} ➞ 6')
print(f'{overlapping_rectangles([ 2, -9, 11, 5 ], [ 5, -11, 2, 9 ])} ➞ 10')
print(f'{overlapping_rectangles([ -8, -7, 4, 7 ],  [-5, -9, 4, 7 ]) }➞ 5')