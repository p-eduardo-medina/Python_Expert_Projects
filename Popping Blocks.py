from itertools  import groupby as gb
def final_result(lst):
    while len(lst)>1:
        if not any( lst[i]==lst[i+1] for i in range( len(lst)-1 ) ): return lst
        groups = [[key, list(group)] for key, group in gb(lst) ] 
        popel = max(groups, key=lambda x: len(x[1]), default=None)
        goodindex = next( (i for i in range(len(lst)) if lst[i:i+len(popel[1])] == [popel[0]]*len(popel[1])), None)
        lst = lst[:goodindex ] + lst[goodindex+len(popel[1]):]
    return lst

#Las tuplas pueden ser utilizadas como iteradores
    
##popel = max(gb(lst), key = lambda x: len( tuple(x[1]) ) )  
#numbers = [10, 25, 30, 45, 50]
# Find the first index where the number is greater than 28
#index = next((i for i, val in enumerate(numbers) if val > 28), None)

print(f'{final_result(["B", "B", "A", "C", "A", "A", "C"])} ➞ ["A"]')
print(f'{final_result(["B", "B", "C", "C", "A", "A", "A"])} ➞ []')
print(f'{final_result(["C", "A", "C"])} ➞ ["C", "A", "C"]')