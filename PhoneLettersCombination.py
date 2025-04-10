#Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.

def letter_combinations(digits):
    dictPhone = {1:[''],
                 2:['a','b','c'],
                 3:['d','e','f'],
                 4:['g','h','i'],
                 5:['j','k','l'],
                 6:['m','n','o'],
                 7:['p','q','r'],
                 8:['t','u','v'],
                 9:['w','x','y','z']}
    lstResponse = []
    for index, char in enumerate(digits):        
        for letter in dictPhone[int(char)]:
            for auxCHar in digits[index+1:] : 
                strResponse = letter
                for auxletter in dictPhone[int(auxCHar)]: 
                    strResponse+=auxletter
                lstResponse.append(auxletter)
    return lstResponse
                
                    
            
            
        

#print(letter_combinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], "")
print(f'{letter_combinations("532")} \n\n {["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]}')
#print(letter_combinations("943"), ["wgd", "wge", "wgf", "whd", "whe", "whf", "wid", "wie", "wif", "xgd", "xge", "xgf", "xhd", "xhe", "xhf", "xid", "xie", "xif", "ygd", "yge", "ygf", "yhd", "yhe", "yhf", "yid", "yie", "yif", "zgd", "zge", "zgf", "zhd", "zhe", "zhf", "zid", "zie", "zif"], "")