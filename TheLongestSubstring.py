"""Given a string of letters, create a function that returns a list with the separator 
that yields the longest possible substring, provided that:

The substring starts and ends with the separator.
The separator doesn't occur inside the substring other than at the ends.
If two or more separators yield substrings with the same length,
they should appear in alphabetical order.
"""

def max_separator(txt):
    dictSubList = {}
    for index,char in enumerate(txt):
        if char not in dictSubList.keys():
            dictSubList[char] = char
            if txt[index:].count(char)>1: 
                for i in range(index+1,len(txt)):
                    dictSubList[char] += txt[i]
                    if txt[i] == char: break
        else:
            newStr = char
            if txt[index:].count(char)>1: 
                for i in range(index+1,len(txt)):
                    newStr += txt[i]
                    if txt[i] == char:
                        if len(newStr)>len(dictSubList[char]):
                            dictSubList[char] = newStr
                            break
    maxLeng = len(max(dictSubList.values(), key=len))
    ansList = []
    if maxLeng>1:
        for key,values in dictSubList.items():
            if len(values)==maxLeng:
                ansList.append(key)
    return ansList
                    
                

    


print(max_separator("supercalifragilistic"), ["s"])
print(max_separator("laboratory"), ["a", "o", "r"])
print(max_separator("candle"), [])
print(max_separator("eagle"), ["e"])
print(max_separator("acquaintance"), ["c"])
print(max_separator("bookkeeper"), ["e"])
print(max_separator("couple"), [])
print(max_separator("slippery"), ["p"])
print(max_separator("address"), ["d", "s"])
print(max_separator("tatertot"), ["t"])
print(max_separator("transmissive"), ["i", "s"])
print(max_separator("stereotype"), ["e", "t"])

print(max_separator("pedroeuardomedinagonzalez"))