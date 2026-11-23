def coins_div(lst):
	trg=sum(lst)//3
	p=[trg,trg,trg]
	for i in sorted(lst,reverse=True):
		if  i-p[0]==0:
			p[0]-=i
		elif i-p[1]==0:
			p[1]-=i
		elif i-p[2]==0:
			p[2]-=i
		else:
			p[2]-=i
		p.sort()
	return p[0]==p[2]


print(f'{coins_div([1, 2, 3, 2, 2, 2, 3])} ➞ True')
print(f'{coins_div([5, 3, 10, 1, 2])} ➞ False')
print(f'{coins_div([2, 4, 3, 2, 4, 9, 7, 8, 6, 9])} ➞ True')