"""Given a string of letters, create a function that returns a list with the separator 
that yields the longest possible substring, provided that:

The substring starts and ends with the separator.
The separator doesn't occur inside the substring other than at the ends.
If two or more separators yield substrings with the same length,
they should appear in alphabetical order.
"""

def max_separator(txt):
    pass

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