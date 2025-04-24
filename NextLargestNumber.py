# Write a function that returns the next number
# that can be created from the same digits as the input.

import itertools
def next_number(num):
    lstNums = list(str(num))
    permutationNums = list(set([int(''.join(permutation)) for permutation in itertools.permutations(lstNums)]))
    permutationNums = [number for number in permutationNums if number!=num]
    dictDiffNumbers = dict()
    for Num in permutationNums: 
        if Num>num: dictDiffNumbers[Num] = abs(num-Num)
    if not dictDiffNumbers: return num
    minValue = min(dictDiffNumbers.values())
    minValues = [key for key,value in dictDiffNumbers.items() if value == minValue]
    return minValues[0]

print(next_number(7) == 7)
print(next_number(19) == 91)
print(next_number(217) == 271)
print(next_number(899) == 989)
print(next_number(989) == 998)
print(next_number(1115) == 1151)
print(next_number(2345) == 2354)
print(next_number(3542) == 4235)
print(next_number(5432) == 5432)
print(next_number(57812) == 57821)
print(next_number(57218) == 57281)
print(next_number(58943) == 59348)
print(next_number(97410) == 97410)
print(next_number(718293) == 718329)
print(next_number(618921) == 619128)
print(next_number(967432) == 972346)
print(next_number(890124) == 890142)
print(next_number(9321345) == 9321354)
print(next_number(219034567) == 219034576)
print(next_number(219876543) == 231456789)