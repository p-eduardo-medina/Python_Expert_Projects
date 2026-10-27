def ecg_seq_index(n):
    ecgSequence = [1, 2]
    nextNumber = 3
    while True:
        if nextNumber in ecgSequence:
            nextNumber += 1
            continue
        n_factors = get_prime_factors_powers(nextNumber)
        next_factors = get_prime_factors_powers(ecgSequence[-1])
        if not set(n_factors).isdisjoint(list(next_factors)):
            ecgSequence.append(nextNumber)
            nextNumber = 3
        else:
            nextNumber += 1 
        if n in ecgSequence:
            break
    return len(ecgSequence)-1

def get_prime_factors_powers(n) -> dict:
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
    return list(factors.keys())

print(ecg_seq_index(3))
print(ecg_seq_index(5))
print(ecg_seq_index(7))