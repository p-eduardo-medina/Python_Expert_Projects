def extended_gcd(a, b):
    """Returns (gcd, x, y) such that a*x + b*y = gcd"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_linear_diophantine(a, b, c):
    """Finds a particular solution to ax + by = c"""
    gcd, x0, y0 = extended_gcd(abs(a), abs(b))
    
    # A solution exists if and only if gcd divides c
    if c % gcd != 0:
        return None  # No integer solutions
    
    # Adjust signs if inputs were negative
    x0 *= 1 if a >= 0 else -1
    y0 *= 1 if b >= 0 else -1
    
    # Scale up the base solution to match c
    factor = c // gcd
    return x0 * factor, y0 * factor

# Example: Solve 2x + 3y = 5
print(solve_linear_diophantine(2, 3, 5))  # Output: (-5, 5) -> (2*-5 + 3*5 = 5)