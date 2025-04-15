def num_regions(grid):
    import numpy as np
    grid = np.array(grid, dtype=np.int32)
    dictOfRegions = dict()
    count = 0
    for  row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                NotinSet = True
                for key, Coords in dictOfRegions.items():
                    flag = False
                    for Coord in Coords:
                        if abs(Coord[0]-row) <= 1 ^ abs(Coord[1]-column)<=1:  # ^ Means the XOR Gate
                            dictOfRegions[key].append([row,column])
                            flag = True
                            NotinSet = False
                            break
                if NotinSet:
                    dictOfRegions[count] =[[row,column]]
                    count+=1
            if not bool(dictOfRegions): 
                dictOfRegions[count] =[[row,column]]
                count+=1
    listKeys = set()
    for key, coords in dictOfRegions.items():
        for subKey,SubCoords in dictOfRegions.items():
            if any(coord in SubCoords for coord in coords):
                if key != subKey: 
                    listKeys.append(set([key,subKey]))
    print(listKeys)
    return len(dictOfRegions)

def XOR(A, B):
	return A ^ B
 
print(num_regions([
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]]), 1)
print(num_regions([
    [1, 1, 1, 1, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1]]), 2)
print(num_regions([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1]]), 3)