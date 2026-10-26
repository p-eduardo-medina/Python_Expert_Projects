def is_economical(n):
  count = 0
  for base,power in get_prime_factors_powers(n).items():
    count += len(str(base))
    if power > 1: count += len(str(power))
  if len(str(n)) == count:
    return "Equidigital"
  elif len(str(n)) > count:
    return "Frugal"
  else:
    return "Wasteful"

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

print(is_economical(14))
print(is_economical(125))
print(is_economical(1024))
print(is_economical(30))