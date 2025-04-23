# The Vigenere Cipher is a poly-alphabetic 
# substitution cipher that uses a set of 
# shift ciphers and a keyword.
import math
def vigenere(text, keyword):
    text = text.upper()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    MatrixCipher = [list(alphabet)]
    for row in range(len(alphabet)-1): MatrixCipher.append( [ MatrixCipher[row][index%len(alphabet)] for index in range(1,len(alphabet)+1) ] )
    text = ''.join([char for char in text if char in alphabet ])
    rate, residue = math.floor(len(text)/len(keyword)), len(text) % len(keyword)
    key = keyword*rate + keyword[:residue]
    key = key.upper()
    Ciphertext = ''
    for index,charPlaintext in enumerate(text):
        charKey = key[index]
        column = MatrixCipher[0].index(charPlaintext)
        row = [indexRow for indexRow in range(len(MatrixCipher)) if  MatrixCipher[indexRow][0]==charKey]
        row = row[0]
        Ciphertext += MatrixCipher[row][column]
    return Ciphertext
    



t1 = "Soylent Green is people."
t2 = "Darth Vader is Luke's father."
t3 = 'Malcolm Crowe was dead the whole time.'

print(vigenere(t1, 'spoiler')== 'KDMTPRKYGSMYMJHTCXWI')
print(vigenere(t2, 'spoiler')== 'VPFBSZRVTFQDPLCTGNLXYWG')
print(vigenere(t3, 'edabit')== 'QDLDWEQFRPEXADSEMTHWHFEASOEUQFI')