def number_sequence(n):
    if n<=0:return "-1"
    elif n==1: return "1"
    def numSeq(sn):
        if sn == 2 : return [1, 1]
        subS = numSeq(sn-1)
        if sn%2==1 : subS = [x+1 for x in subS]
        subS.insert(len(subS)//2,1)
        return subS
    return ' '.join(str(s) for s in numSeq(n))
    

print(number_sequence(99))