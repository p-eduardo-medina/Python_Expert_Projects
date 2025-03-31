def getpolyBus():
    dictPolyBus={}
    import string
    lowercase_alphabet = string.ascii_lowercase
    for i in range(5):
        for j in range(5):
            if lowercase_alphabet[0] != 'j':
                dictPolyBus[lowercase_alphabet[0]] = [i+1,j+1]
                lowercase_alphabet= lowercase_alphabet[1:len(lowercase_alphabet)]
            else:
                dictPolyBus[lowercase_alphabet[0]] = [i+1,j]
                dictPolyBus[lowercase_alphabet[1]] = [i+1,j+1]
                lowercase_alphabet = lowercase_alphabet[2:len(lowercase_alphabet)]
    return dictPolyBus

def polybius(text): 
    import string
    alphabet = string.ascii_lowercase
    dictPolybus = getpolyBus()
    message =''
    if text[0].lower() in alphabet:
        text = text.lower()
        for char in text:
            if char in alphabet:
                message+=str(dictPolybus[char][0])+str(dictPolybus[char][1])
            elif(char==' '):
                message+=char
    else:
        i = 0
        while i<len(text):
            if text[i]!=' ':
                char = [int(text[i]), int(text[i+1])]
                for key, value in dictPolybus.items():
                    if char ==value:
                        message+=key
                        i+=2
                        break
            else:
                message+=' '
                i+=1
            
    return message
        
                
            
        
        
booleanResp = polybius("Hi")=="2324"
print(booleanResp)
booleanResp = polybius("Just because I dont care doesnt mean that I dont understand") == '24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314'
print(booleanResp)
booleanResp = polybius("2324 4423154215")=="hi there"
print(booleanResp)
booleanResp = polybius("543445 14343344 522433 21422415331443 52244423 4311311114")=="you dont win friends with salad"
print(booleanResp)
print(polybius('543445 14343344 522433 21422415331443 52244423 4311311114')=="you dont win friends with salad")
#print(f'{polybius("543445 14343344 522433 21422415331443 52244423 4311311114")}/"you dont win friends with salad"')