""" The formula for calculating nPr is n!/(n-r)! ("!" is the factorial operation).
The formula for calculating nCr is n!/(r!(n-r)!). 
Your functions should work efficiently for cases where n! or r! are very 
large compared to the result. Simply calculating the factorials and 
dividing will cause your program to time out. 
See if you can think of a more efficient method.
"""
def nPr(n, r):#n!/(n-r)!
  value = 1
  for i in range(n - r + 1, n + 1):value *= i
  return value

def nCr(n, r):#n!/(r!(n-r)!)
	if n-r < r: r = n-r	
	value = nPr(n, r)
	for i in range(1, r + 1):value //= i
	return value


###Try next
###Use the symmetry nCr(n, r) = nCr(n, n-r) to work with the smaller selection count, 
# then cancel denominator factors during the calculation instead of building a full factorial.
testsP = [
	((7, 4), 840),
	((8, 5), 6720),
	((4, 3), 24),
	((7, 7), 5040),
	((7, 1), 7),
	((300, 3), 26730600),
	((1000000, 2), 999999000000),
	((1000000000, 1), 1000000000),
]

testsC = [
	((7, 4), 35),
	((8, 5), 56),
	((4, 3), 4),
	((7, 7), 1),
	((7, 1), 7),
	((300, 3), 4455100),
	((300, 297), 4455100),
	((1000000, 2), 499999500000),
	((1000000, 999998), 499999500000),
	((1000000000, 1), 1000000000),
	((1000000000, 1000000000), 1),
]
print('Testing Permuations')
for test in testsP:
	print("Input: " + str(test[0]))
	print(nPr(*test[0])== test[1])
print('Testing Combinations')
for test in testsC:
	print("Input: " + str(test[0]))
	print(nCr(*test[0]) == test[1]) 