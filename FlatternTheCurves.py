# The nesting of lists can be viewed indirectly 
# as curves and barriers of the real data embedded
# in lists, thus, defeats the very purpose of directly
# accessing them thru indexes and slices. In this challenge,
# a function is required to flatten those curves (i.e. level,
# iron, compress, raze, topple) and expose those data as a single
# list and not as a list of lists.
def flatten(r):
    return AuxFlattern(r,[])

def AuxFlattern(r, responsearr):
    if type(r) == list:
        for element in r:
            responsearr = AuxFlattern(element,responsearr)
    else:
        responsearr.append(r)
    return responsearr



#print(f'{flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])} // ["direction", 372, "one", "Era", "Sruth", 3337, "First"]')



arr_vectors = [
  [[[[[['direction'], [372], ['one'], [[[[[['Era']]]], 'Sruth', 3337]]], 'First']]]],
  [[4666], [5394], [466], [[['Saskia', [[[[['DXTD']], 'Lexi']]]]]]],
  [[696], ['friend'], ['power'], [[[['Marcus']]]], ['philus']],
  [[['deep'], [[['ocean']]], [['Marge']], ['rase', 876]]],
  ['I', [19.79, 'love', [12.17], "edabit"]], 
  [['The', ['first', ['of', ["May", 0.0, 1, ]]], 2, 3, 4]],
  [7, [11, 'lived', [[229]]]], 
  ['and', 6, [3, 'scores', ['six', 100]]]]
res_vectors = [
  ['direction', 372, 'one', 'Era', 'Sruth', 3337, 'First'],
  [4666, 5394, 466, 'Saskia', 'DXTD', 'Lexi'],
  [696, 'friend', 'power', 'Marcus', 'philus'],
  ['deep', 'ocean', 'Marge', 'rase', 876],
  ['I', 19.79, 'love', 12.17, 'edabit'],
  ['The', 'first', 'of', 'May', 0.0, 1, 2, 3, 4],
  [7, 11, 'lived', 229],
  ['and', 6, 3, 'scores', 'six', 100]
]

for i, r in enumerate(arr_vectors):
  print(flatten(r) == res_vectors[i] ,flatten(r), res_vectors[i])