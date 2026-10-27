def freq_count(lst, el):
	level = 0
	anw = []
	while lst:
		anw.append([level, lst.count(el)])
		level += 1
		lst = [
			x for item in lst if isinstance(item,list)
            for x in item 
            ]
	return anw
    
print(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)==[[0, 1], [1, 2], [2, 3]])
print(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)==[[0, 3], [1, 4], [2, 0]])
print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)==[[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]])