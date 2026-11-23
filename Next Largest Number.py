def next_number(num):
    nums = list(str(num))
    if all(int(a) >= int(b) for a, b in zip(nums, nums[1:])) or len(nums)==1: return num
    for i in range(2,len(nums)+1):
        if int(''.join(nums[:-i] + sorted(nums[-i:],reverse=True)) ) > num:
            auxSort,auxn = nums[:-i].copy(),nums[-i:].copy()
            pos = min([ [i,n] for i,n in enumerate(auxn[1:]) if int(n) >= int(auxn[0]) ], 
                                    key=lambda x: x[1])# +=1 
            auxSort += auxn[pos[0]+1]
            auxn = auxn[:pos[0]+1]+auxn[pos[0]+2:]
            return int(''.join(auxSort + sorted(auxn)) )
    

print(f'{next_number(19) }➞ 91')
print(f'{next_number(3542) }➞ 4235')
print(f'{next_number(5432) }➞ 5432')
print(f'{next_number(58943) }➞ 59348')