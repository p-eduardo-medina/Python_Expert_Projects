def extract_primes(num):
   outList = [
                int(str(num)[i:len(str(num))-j]) for i in range(len(str(num)))
                for j in range(len(str(num))-i) 
                if is_prime(int(str(num)[i:len(str(num))-j])) and int(str(num)[i:len(str(num))-j])!=1 and str(num)[i:len(str(num))-j][0]!="0"
              ]
   return sortArray(outList)  

import math
def is_prime(p) -> bool:
    return p > 1 and all( p%index != 0 for index in range( 2 , int(p**0.5 + 1) ) )

def sortArray(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[int(len(arr)/2)]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    grater = [x for x in arr if x > pivot]
    return sortArray(smaller) + equal + sortArray(grater)

print(extract_primes(1))
print(extract_primes(7))
print(extract_primes(73))
print(extract_primes(103))
print(extract_primes(1313))
