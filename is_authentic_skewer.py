def is_authentic_skewer(word):
    consonants = "bcdfghjklmnpqrstvwxyz".upper()
    vowels = "aeiou".upper()
    alphabet = vowels+consonants
    space = ""
    
    if not(word[0] in consonants or word[len(word)-1] in consonants):
        return False
    for i in range(1,len(word)):
        if not( word[i] in alphabet ):
            space+=word[i]
        else:
            break
    
    if(space==""):return False
    word = word.split(space)
    Flag = 'v'
    for element in word:
        if not(element in alphabet):
            return False
        else:
            if element in consonants:
                if Flag =='c':
                    return False
                else:
                    Flag='c'
            if element in vowels:
                if Flag =='v':
                    return False
                else:
                    Flag='v'
    return True
                
  

        

print(is_authentic_skewer("BANANAS"))


