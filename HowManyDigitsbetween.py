def digits(n):
    l = len(str(n))
    print(n * l , int('1' * l),n * l - int('1' * l))
    return n * l - int('1' * l)
        
 

print(digits(103496754) == 820359675)
print(digits(3248979384) == 31378682729)
print(digits(122398758003456) == 1724870258940729)
print(digits(58473029386609125789) == 1158349476621071404669)


print(f'{digits(1)} ➞ 0')
print(f'{digits(10)} ➞ 9')
print(f'{digits(100)} ➞ 189')
print(f'{digits(2020)} ➞ 6969')


print(digits(1) == 0)
print(digits(10) == 9)
print(digits(100) == 189)
print(digits(2020) == 6969)