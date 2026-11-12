from itertools  import groupby as gb
def final_result(lst):
    sl = gb(lst)
    for k,l in sl:
        print(k,l)


print(f'{final_result(["B", "B", "A", "C", "A", "A", "C"])} ➞ ["A"]')
print(f'{final_result(["B", "B", "C", "C", "A", "A", "A"])} ➞ []')
print(f'{final_result(["C", "A", "C"])} ➞ ["C", "A", "C"]')