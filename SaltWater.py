import math
def salt(t):
    return round(1 + 9*math.exp((-0.1)*t), 3)

print(salt(0))
print(salt(5))
print(salt(10))
print(salt(120))
