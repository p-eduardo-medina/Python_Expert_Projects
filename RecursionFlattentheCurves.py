def flatten(r):
  r = [element for val in r for element in (val if isinstance(val, list) else [val]) ]
  if any(isinstance(x,list) for x in r):return flatten(r)
  return r




print(f'{flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])}➞ ["direction", 372, "one", "Era", "Sruth", 3337, "First"]')
print(f'{flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]])}➞ [4666, 5394, 466, "Saskia", "DXTD", "Lexi"]')
print(f'{flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]])}➞ [696, "friend", "power", "Marcus", "philus"]')
print(f'{flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])}➞ ["deep", "ocean", "Marge", "rase", 876]')
