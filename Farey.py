def farey(n):
    fraction = []
    fraction.append(f"0/1")
    for i in range(2, n+1):
        for j in range(1, i):
            NumFtr, DenFact = get_prime_factors_powers(j), get_prime_factors_powers(i)
            commonFactors = {key: min(NumFtr[key], DenFact[key]) for key in NumFtr if key in DenFact}
            gdc = 1
            for factor in commonFactors:
                gdc *= factor**commonFactors[factor]
            if gdc == 1:
                fraction.append(f"{j}/{i}")
    fraction.append(f"{1}/{1}")
    fraction = quicksort(fraction)
    return fraction


def get_prime_factors_powers(n) -> dict:
    if n ==0: return {0:1}
    if n ==1: return {1:1}
    import math
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i            
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors

def quicksort(arr):
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
    
    # Pick a pivot (choosing the middle minimizes worst-case risks)
    pivot = arr[len(arr) // 2]
    pvtNum,pvtDen = pivot.split('/')
    
    # Partition elements into three distinct groups
    left,right,middle = [],[],[]
    for x in arr:
        num, den = x.split('/')
        if int(num) * int(pvtDen) < int(pvtNum) * int(den):
            left.append(x)
        elif int(num) * int(pvtDen) > int(pvtNum) * int(den):
            right.append(x)
        else:
            middle.append(x)
    
    # Recursively sort the outer groups and combine them
    return quicksort(left) + middle + quicksort(right)


print(farey(5))