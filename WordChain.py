def isWordChain(words):
    while len(words)>1:
        if abs(len(words[0])-len(words[1]))>1:return False
        elif len(words[0])==len(words[1]):
            if sum(words[0][c]!=words[1][c] for c in range(len(words[0])))>1: return False
            words.pop(0)
            continue
        if len( set(list(words[0]))^set(list(words[1])) )>1:return False
        else:words.pop(0)
    return True

print(f'{isWordChain(["row", "crow", "crown", "brown", "brawn"])} ➞ True')
print(f'{isWordChain(["flew", "flaw", "flan", "flat", "fat", "rat", "rot", "tot"])} ➞ True')
print(f'{isWordChain(["meek", "meet", "meat", "teal"])} ➞ False')
print(f'{isWordChain(["run", "runny", "bunny"])} ➞ False')