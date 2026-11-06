def zero_indices(lst, k):
	ind = [i for i in range(len(lst)) if lst[i]==0]+[len(lst)]
	if len(ind)==k: return ind
	auxPot = []
	for j in range(len(ind)-k):
		if j==0: 
			auxPot.append(sum(lst[:ind[k]]))
		else:
			auxPot.append(sum(lst[ind[j-1]:ind[j+k]]))
	pot = [sum(lst[:ind[j+k]]) if j==0 else sum(lst[ind[j-1]:ind[j+k]]) for j in range(len(ind)-k)]
	x = pot.index(max(pot))
	return ind[x:x+k]



#count = max((sum(1 for _ in g) for k, g in groupby(ausLst) if k == 1), default=0)
#data = sorted([1, 1, 2, 2, 2, 3, 1, 1]) <-- <-- <-- <-- <-- <--<-- <-- <-- <-- <-- <-- SORTED()
## Group and print
#for key, group in groupby(data):
#    print(f"Key: {key}, Group: {list(group)}")
#Key: 1, Group: [1, 1, 1, 1]
#Key: 2, Group: [2, 2, 2]
#Key: 3, Group: [3]


#ausList = [1, 1, 2, 2, 2, 3, 1, 1]
#for k, g in groupby(ausList):
#    print(k,list(g))
#    
#1 [1, 1]
#2 [2, 2, 2]
#3 [3]
#1 [1, 1]

print(f'{zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) }➞ [1]')
print(f'{zero_indices([1, 0, 0, 0, 0, 1], 1)} ➞ [1]')
print(f'{zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3)} ➞ [6, 7, 9]')
print(f'{zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3)} ➞ [7, 8, 9]')
