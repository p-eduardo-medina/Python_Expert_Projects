def is_authentic_skewer(s):
  consonants,vowels = "bcdfghjklmnpqrstvwxyz".upper(),"AEIOU"
  alphabet = consonants+vowels
  if s[0] not in consonants or s[-1] not in consonants:
    return False
  arrS = [ index for index in range(len(s)) if s[index] in alphabet]
  if not all( arrS[index + 1] -  arrS[index] == arrS[1] - arrS[0] for index in range( len(arrS)-1 ) ) : 
    return False
  if not all( (s[arrS[index]] in vowels)^(s[arrS[index + 1]] in vowels) for index in range(len(arrS) - 1) ):
    return False
  return True



print(is_authentic_skewer("B--A--N--A--N--A--S"))
print(is_authentic_skewer("A--X--E"))
print(is_authentic_skewer("C-L-A-P"))
print(is_authentic_skewer("M--A---T-E-S"))