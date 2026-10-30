"""Given a string of letters, create a function that returns a list with the separator 
that yields the longest possible substring, provided that:

The substring starts and ends with the separator.
The separator doesn't occur inside the substring other than at the ends.
If two or more separators yield substrings with the same length,
they should appear in alphabetical order.
"""

def max_separator(txt):
    output,maxSS = {},0
    for index in range(len(txt)-1):
        for auxIndex in range(index+1, len(txt)):
            if txt[index] == txt[auxIndex]:
                if auxIndex-index >= maxSS:
                    output[txt[index]] = auxIndex-index
                    maxSS = auxIndex-index
                break
    if output:maxVaalue = max(output.values())
    return sorted( [key for key,value in output.items() if value==maxVaalue] )

    
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
