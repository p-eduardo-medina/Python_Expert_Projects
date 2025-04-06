# Write a function that connects each previous 
# word to the next word by the shared letters. 
# Return the resulting string (removing duplicate
# characters in the overlap) and the minimum number
# of shared letters across all pairs of strings.

import math
def join(lst):
    ansString = lst[0]
    minimunIndex = math.inf
    for index in range(len(lst)-1):
        savedIndex = 0
        word = lst[index]
        for i in range(len(word)+1):
            if word[len(word)-i:] ==  lst[index+1][:i]:
                savedIndex = i
        if savedIndex<minimunIndex:
            minimunIndex = savedIndex
        ansString+= lst[index+1][savedIndex:]
    return ansString, minimunIndex
                

print(set(join(["happy", "python", "honey", "yelp", "plank", "lanky"]))== set(["happythoneyelplanky", 1]))
print(join(["move", "over", "very"]),["movery", 3])
print(join(["oven", "envier", "erase", "serious"]),["ovenvieraserious", 2])
print(join(["to", "ops", "psy", "syllable"]),["topsyllable", 1])
print(join(["aaa", "bbb", "ccc", "ddd"]),["aaabbbcccddd", 0])
print(join(["abcde", "bcdefghi", "efghi", "fghij", "ghijklmnop"]),["abcdefghijklmnop", 4])
print(join(["aab", "abcccd", "cdeeef", "effff"]),["aabcccdeeeffff", 2])