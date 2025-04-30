# Given a list of coins, father needs to distribute 
# them amongst his three children. Write a function 
# to determine if the coins can be distributed equally 
# or not. Return True if each son receives the same 
# amount of money, otherwise return False.
import itertools
def coins_div(lst):
    lstPermutations = list(set(itertools.permutations(lst)))
    dividedAmount = sum(lst)/3
    if not dividedAmount.is_integer(): return False
    for permutation in lstPermutations:
        updatedSum = 0
        count=0
        for num in permutation:
            updatedSum+=num
            if updatedSum>dividedAmount: break
            elif updatedSum == dividedAmount: 
                count+=1
                updatedSum = 0
        if count==3: return True
    return False
    
print(coins_div([1, 1, 1]), True)
print(coins_div([80, 78, 79, 65, 61]), False)
print(coins_div([1, 1, 1]), True)
print(coins_div([80, 78, 79, 65, 61]), False)
print(coins_div([1, 2, 3, 2, 2, 2, 3]), True)
print(coins_div([5, 3, 10, 1, 2]), False)
print(coins_div([2, 4, 3, 2, 4, 9, 7, 8, 6, 9]), True)
print(coins_div([4, 7, 6, 8, 2, 1, 2]), True)
print(coins_div([3, 6, 2, 2, 2, 2, 1, 3, 2, 1, 3]), True)
print(coins_div([11, 9, 3, 22, 6, 2, 4, 10, 1]), False)
print(coins_div([13, 6, 12, 23, 2, 8, 15, 31, 16]), False)
print(coins_div([4, 14, 12, 21, 3, 1, 18, 5]), True)
print(coins_div([10, 5, 20, 27, 17, 4, 3, 15, 0, 25]), True)
print(coins_div([1, 13, 10, 6, 24, 16, 22, 4]), False)
print(coins_div([9]), False)
print(coins_div([246, 96, 129, 220, 203, 75, 200, 77, 114, 91]), False)
print(coins_div([3, 2, 2, 5, 9, 3, 3]), True)