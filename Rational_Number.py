def division(a, b):
    from decimal import Decimal
    a = Decimal(a)
    b = Decimal(b)
    div = str(a/b)
    point = div.index('.')
    pattern = ''
    repS,rep  = 1,0
    for i in div[point+1:]:
        PATTERNS = []
        for index in range(len(pattern)):
            PATTERNS.append(pattern[index:])
        for patt in PATTERNS:
            rep = div[point+1:].count(patt)
            if rep>repS:    
                pattern = patt
                repS = rep
        patternStar = div[point+1:].find(pattern)
        if rep*len(pattern)>=len(div[point+1:][patternStar:])-len(pattern):
            break
        pattern +=i    
    if rep*len(pattern)==len(div[point+1:])-len(pattern):return div[0:div.find(pattern)]+ str(pattern)
    else:return div[0:div.find(pattern)]+ '(' + str(pattern) +')'


print(f'Calculate solution ➞ {division(2, 5)} || Expected Solution ➞ "0.4"')
print(f'Calculate solution ➞ {division(1, 6)} || Expected Solution ➞ "0.1(6)"')
print(f'Calculate solution ➞ {division(1, 3)} || Expected Solution ➞ "0.(3)"')
print(f'Calculate solution ➞ {division(1, 7)} || Expected Solution ➞ "0.(142857)"')
print(f'Calculate solution ➞ {division(1, 77)} || Expected Solution ➞ "0.(012987)"')