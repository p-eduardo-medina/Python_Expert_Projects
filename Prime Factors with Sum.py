import math
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def getPrimes(n: int) -> list[int]:
    primes = []
    candidate, index = 2, 2
    while index <= n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
        index += 1
    return primes

def sum_prime(lst):
    primes = getPrimes(max(lst))
    my_dict = {prime: sum( num for num in lst if num % prime==0) for prime in primes}
    my_dict = {k: v for k, v in my_dict.items() if v > 0}
    return ''.join(["("+str(k)+ " " +str(v) +")" for k,v in my_dict.items() ])
    





print(f'{sum_prime([12, 15])} ➞ (2 12)(3 27)(5 15)')
print(f'{sum_prime([7, 13, 18, 23, 24])} ➞ (2 42)(3 42)(7 7)(13 13)(23 23)')
print(f'{sum_prime([3, 5, 7, 9, 11, 13])} ➞ (3 12)(5 5)(7 7)(11 11)(13 13)')