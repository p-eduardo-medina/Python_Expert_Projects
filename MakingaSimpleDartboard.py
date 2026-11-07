def make_dartboard(n):
  dB = [[1]*n]
  for i in range(1,int((n+1)/2)): dB.append( [ dB[-1][x]+1 if x>=i and x<n-i else dB[-1][x] for x in range(n)] )
  dB = dB+dB[::-1] if n%2==0 else dB[:-1]+dB[::-1]
  return [ int("".join(str(num) for num in numbers)) for numbers in dB ]

print(make_dartboard(1))
print(make_dartboard(2))
print(make_dartboard(3)) #Eliminar si son impares
print(make_dartboard(8))
print(make_dartboard(5))