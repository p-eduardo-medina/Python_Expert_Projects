import itertools as it
def is_wristband(lst):
    if all(el ==row[0] for row in lst for el in row): return True
    column_elements = [el for el in lst[0]]
    if all(el == column_elements for el in lst): return True
    flagBR ,flagBL = True, True
    for i, j in it.product(range(len(lst)), range(len(lst[0]))):
        if i+1<len(lst) and j+1<len(lst[0]):
            if lst[i][j] != lst[i+1][j+1]:flagBR = False
        if i+1<len(lst) and j-1>=0: 
            if lst[i][j] != lst[i+1][j-1]:flagBL = False
    return flagBR or flagBL

print(is_wristband([
  ["A", "A"],
  ["B", "B"],
  ["C", "C"]
]))

print(is_wristband([
  ["A", "B"],
  ["A", "B"],
  ["A", "B"]
]))

print(is_wristband([
  ["A", "B", "C"],
  ["C", "A", "B"],
  ["B", "C", "A"],
  ["A", "B", "C"]
]))

print(is_wristband([
  ["A", "B", "C"],
  ["B", "C", "A"],
  ["C", "A", "B"],
  ["A", "B", "A"]
]))