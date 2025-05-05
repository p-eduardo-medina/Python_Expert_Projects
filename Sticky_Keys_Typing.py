"""
Someone is typing on the sticky keyboard. Occasionally a key
gets stuck and more than intended number of characters of a 
particular letter is being added into the string. The function
input contains original and typed strings. Determine if the
typed string has been made from the original. Return True if 
it is and False if the typed string cannot have been made 
from the original."""
def is_long_pressed(original, typed):
    original, typed = replace_multiple_spaces(original), replace_multiple_spaces(typed)
    lstOriginals, lstTypeds = original.split(' '), typed.split(' ')
    lisOfDict = []
    for index, word in enumerate(lstOriginals): lisOfDict.append((dictOfWord(word), dictOfWord(lstTypeds[index])))
    if any(set(tupleOfDicts[0].keys()) != set(tupleOfDicts[1].keys())  for tupleOfDicts in lisOfDict): return False
    for tupleOfDicts in lisOfDict:
        for key, value in tupleOfDicts[0].items():
            if value>tupleOfDicts[1][key]: return False
    return True

def dictOfWord(word) -> dict:
    dictOfWord = {}
    for char in word: dictOfWord[char] = dictOfWord[char]+1 if char in  dictOfWord else 1
    return dictOfWord

import re
def replace_multiple_spaces(text): return re.sub(r"\s+", " ", text)

from time import perf_counter
tic = perf_counter()

print(is_long_pressed("alex", "aaleex") == True)
print(is_long_pressed("saeed", "ssaaedd") == False)
print(is_long_pressed("leelee", "lleeelee") == True)
print(is_long_pressed("Tokyo", "TTokkyoh") == False)
print(is_long_pressed("laiden", "laiden") == True)
print(is_long_pressed("He rose to prominence following his starring role as Michael Scofield in the Fox series Prison Break",
                      "Hee rose to prominence following his starring role as Michael Scofield in  the Foxx series Prison Break") == False)
print(is_long_pressed("Posts identified as harmful by the algorithm can be referred to human moderators, who choose whether to take further action",
                      "Possts identifiedd ass harmmmmful byy the algorithhm caaaan be referrrrred to human mmmoderators,, wwhoo chooose whettheer too take furrther actiiionn") == True)
print(is_long_pressed("Manufacturers spend huge sums developing their latest four-wheeled fantasies, laden with up-to-the-minute electronic gizmos, which apparently will do everything for you except brush your teeth.", "Manufacturers spend huge sums developing their latest ffour-wheeled fantasies, ladeen with up--to-the--minute electronic gizmos, whiich apparently willl ddo everything for you exept brush your teeth..") == False)
print(is_long_pressed("Four years ago, Volkswagen was a very different company.",
                      "Four years ago Volkswagen waas a veery differentt company.") == False)
print(is_long_pressed("She threw his clothes out the window.",
                      "Shhe ttttthrew hiis ccclothes   ouut thee winnndowww.") == True)

print('t_total = {:.6f}'.format(perf_counter() - tic))