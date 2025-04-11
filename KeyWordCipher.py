# A Keyword Cipher is a monoalphabetic cipher which
# uses a keyword to provide encryption on given string of message.
# Create a function that takes two arguments: 
# a string message and a string key, and returns an encoded message.
# For the encryption key, the keyword is placed at the beginning, 
# followed by the rest of the characters in the alphabet in order
# (in other words, with the keyword characters removed)
def keyword_cipher(key, message):
    desencryptedMessage = ''
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    alphabet = [char for char in alphabet]
    alphabet.sort()
    newAlphabet = dict()
    for char in alphabet:
        newAlphabet[char] = char
    for i in range(len(key)):
        newAlphabet[alphabet[i]] = key[i]
    for i in range(len(message)):
        desencryptedMessage+=newAlphabet[message[i]]
    return desencryptedMessage



print(keyword_cipher("keyword","abc"), "key")
print(keyword_cipher("keyword","xyz"), "vxz")
print(keyword_cipher("keyword","aeiou"), "kobjs")
print(keyword_cipher("purplepineapple","abc"), "pur")
print(keyword_cipher("purplepineapple","xyz"), "xyz")
print(keyword_cipher("purplepineapple","aeiou"), "pebjt")
print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz","abc"), "eta")
print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz","xyz"), "qxz")
print(keyword_cipher("etaoinshrdlucmfwypvbgkjqxz","aeiou"), "eirfg")
print(keyword_cipher("tfozcivbsjhengarudlkpwqxmy","abc"), "tfo")
print(keyword_cipher("tfozcivbsjhengarudlkpwqxmy","tjuukf"), "kjpphi")
print(keyword_cipher("tfozcivbsjhengarudlkpwqxmy","ajqqtb"), "tjuukf")
#print(keyword_cipher("tfozcivbsjhengarudlkpwqxmy","a_bc&*83"), "t_fo&*83")
print(keyword_cipher("mubashir","pakistan"), "lmecpqmj")
print(keyword_cipher("mubashir","edabit"), "samucq")