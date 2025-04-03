def get_subsets(lst, n):
    import itertools
    savedList = []
    for rang in range(1,len(lst)+1):
        lis = itertools.combinations(lst,r=rang)
        for sublist in lis:
            value = 0
            for inedx in sublist:
                value+=inedx
            if value == n:
                savedList.append(list(sublist))
    return savedList


                    
            
     



print(f'{get_subsets([-1, 0, 1, 2], 2)     == [[2], [0, 2], [-1, 1, 2], [-1, 0, 1, 2]]}')
print(f'{get_subsets([-1, 0, 1, 2], 3)     == [[1, 2], [0, 1, 2]]}')
print(f'{get_subsets([1, 2, 3, 4], 5)     == [[1, 4], [2, 3]]}')
print(f'{get_subsets([-1, 0, 1, 2], 4)     == []}')
print(get_subsets([-1, 0, 1, 2], 2) == [[2], [0, 2], [-1, 1, 2], [-1, 0, 1, 2]])
print(get_subsets([-1, 0, 1, 2], 3) == [[1, 2], [0, 1, 2]])
print(get_subsets([1, 2, 3, 4], 5) == [[1, 4], [2, 3]])
print(get_subsets([-1, 0, 1, 2], 4) == [])
print(get_subsets([1, 2, 3, 4, 5, 6], 6) == [[6], [1, 5], [2, 4], [1, 2, 3]])
print(get_subsets([-3, -2, -1, 0, 1, 2, 3], 2)==
 [[2], 
 [-1, 3], 
 [0, 2], 
 [-3, 2, 3], 
 [-2, 1, 3], 
 [-1, 0, 3],
 [-1, 1, 2], 
 [-3, 0, 2, 3], 
 [-2, -1, 2, 3], 
 [-2, 0, 1, 3], 
 [-1, 0, 1, 2], 
 [-3, -1, 1, 2, 3], 
 [-2, -1, 0, 2, 3], 
 [-3, -1, 0, 1, 2, 3]])