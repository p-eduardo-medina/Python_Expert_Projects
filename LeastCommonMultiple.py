def lcm(nums):
    dictPrimeNumbersPowers = {}
    for num in nums:
        primeFactors = get_prime_factors_powers(num)
        for prime in primeFactors:
            if prime not in dictPrimeNumbersPowers:
                dictPrimeNumbersPowers[prime] = primeFactors[prime]
            else:
                dictPrimeNumbersPowers[prime] = max(dictPrimeNumbersPowers[prime], primeFactors[prime])
    result = 1
    for prime, power in dictPrimeNumbersPowers.items():
        result *= prime ** power
    return result

def get_prime_factors_powers(n) -> dict:
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

print(lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(lcm([5]))
print(lcm([5, 7, 11]))
print(lcm([5, 7, 11, 35, 55, 77]))