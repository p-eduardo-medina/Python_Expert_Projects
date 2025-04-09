# Given a rectangular grid of m by n spaces,
# signaled by 0s, and a number of points, 
# signaled by 1, 2, 3..., return the number of
# moves for the shortest path that starts 
# at 1 and goes over all the other points in ascending order.
def shortest_path(lst):
    coordDict = {}
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j]!='0':
                coordDict[int(lst[i][j])] = [int(i),int(j)]
    count = 0
    try:
        diffcoords = coordDict[1]
        indexLst = [i for i in range(2,len(coordDict.keys())+1)]
        for Num in indexLst:
            count += abs(diffcoords[0]-coordDict[Num][0]) + abs(diffcoords[1]-coordDict[Num][1])
            diffcoords = [coordDict[Num][0],coordDict[Num][1]]
    except: None
    return count
            
     
 
 
 
print(shortest_path([
	('00000'),
	('01006'),
	('02000'),
	('30050'),
	('00004')
]),'/' , 13, '6 vertical moves, 7 horizontal moves.')

print(shortest_path([
	('600001'),
  ('002005'),
  ('040073')
]),'/' , 29, '6 vertical moves, 23 horizontal moves.')

print(shortest_path([
	('0000000'),
	('0050000'),
	('0000000'),
	('2030410')
]),'/' ,  13, '2 vertical moves, 11 horizontal moves.')
	
print(shortest_path([
	('00000')
]),'/' ,  0, 'No moves.')
	
print(shortest_path([
	('0020'),
	('0030'),
	('1000')
]),'/' ,  5, '3 vertical moves, 2 horizontal moves.')
	
print(shortest_path([
	('0000'),
	('0010'),
	('0000')
]),'/' ,  0, 'No moves.')
	
print(shortest_path([
	('2'),
	('0'),
	('1')
]),'/' ,  2, '2 vertical moves, 0 horizontal moves.')
	
print(shortest_path([
	('340009'),
	('005007'),
	('060001'),
	('802000'),
	('000000')
]),'/' ,  34, '12 vertical moves, 22 horizontal moves.')