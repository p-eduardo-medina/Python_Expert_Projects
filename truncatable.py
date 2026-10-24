def truncatable(n):
    if "0" in str(n):return False
    flagLeft = all([isprime(int(str(n)[i:])) for i in range(len(str(n)))])
    flagRight = all([isprime(int(str(n)[:i + 1])) for i in range(len(str(n)))])
    if flagRight and flagLeft:
        return "both"
    elif flagRight:
        return "right"
    elif flagLeft:
        return "left"
    else:
        return False

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(truncatable(9137))
print(truncatable(5939))
print(truncatable(317))
print(truncatable(5))
print(truncatable(139))
print(truncatable(103))
