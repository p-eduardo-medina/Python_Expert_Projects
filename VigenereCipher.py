# The Vigenere Cipher is a poly-alphabetic 
# substitution cipher that uses a set of 
# shift ciphers and a keyword.
def vigenere(text, keyword):
    text = text.upper()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    MatrixCipher = [list(alphabet)]
    for row in range(len(alphabet)-1): MatrixCipher.append( [ MatrixCipher[row][index%len(alphabet)] for index in range(1,len(alphabet)+1) ] )
    text = ''.join([c for c in text if c in alphabet ])
    key = keyword*int(len(text)/len(keyword)) + keyword[:(len(text) % len(keyword))]
    key = key.upper()
    Ciphertext = ''
    for index,charPlaintext in enumerate(text):
        column = MatrixCipher[0].index(charPlaintext)
        row = next( (i for i in range(len(MatrixCipher)) if MatrixCipher[i][0]==key[index]) ,None)
        Ciphertext += MatrixCipher[row][column]
    return Ciphertext
    



t1 = "Soylent Green is people."
t2 = "Darth Vader is Luke's father."
t3 = 'Malcolm Crowe was dead the whole time.'

print(vigenere(t1, 'spoiler') == 'KDMTPRKYGSMYMJHTCXWI')
print(vigenere(t2, 'spoiler') == 'VPFBSZRVTFQDPLCTGNLXYWG')
print(vigenere(t3, 'edabit') == 'QDLDWEQFRPEXADSEMTHWHFEASOEUQFI')