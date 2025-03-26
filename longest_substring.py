def longest_substring(digits):
    listNums = []
    subString = ""
    
    for i,digit in enumerate(digits[:len(digits)-1]):          
        subString+=digit
        if (int(digit)-int(digits[i+1]))%2!=1:            
            listNums.append(subString)
            subString = ""
        else:
            if i==len(digits)-2:         
                listNums.append(subString+digits[len(digits)-1])     
    value,maxLen = 0,0
    for i in listNums:
        if(maxLen < len(i)):
            maxLen = len(i)
    for i,num in enumerate(listNums):
        if len(num)==maxLen:
            value = i
            break
    
    return listNums[value]

            
            
            
print(longest_substring("754388489999793138912431545258") )# "545258"
print(longest_substring("594127169973391692147228678476")) # "16921472"
print(longest_substring("721449827599186159274227324466")) # "7214"