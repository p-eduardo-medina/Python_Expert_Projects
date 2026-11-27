def dice_roll(n, outcome):
    succes = 0
    for i in range(6**n):
        i0, lstDices = i,[]
        for _ in range(1,n+1):
            lstDices.append(i0%6+1)
            i0=i0//6
        if sum(lstDices)==outcome:succes+=1
    return succes        
    

print(f'{dice_roll(1, 3)} == 1', "1")
print(f'{dice_roll(2, 5)} == 4', "4")
print(f'{dice_roll(3, 4)} == 3', "3")
print(f'{dice_roll(4, 18)} == 80', "80")
print(f'{dice_roll(6, 20)} == 4221', "4221")