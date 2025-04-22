# Write a function that returns the 
# longest non-repeating substring for a string input.
def longest_nonrepeating_substring(txt):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lstStrings = []
    longestSubString = txt[0]
    for index,char in enumerate(txt[1:len(txt)]):
        currentIndex = alphabet.find(longestSubString[len(longestSubString)-1])
        nextIndex = alphabet.find(char)
        if currentIndex<nextIndex:
            longestSubString+=alphabet[nextIndex]
        else:
            lstStrings.append(longestSubString)
            longestSubString = char
        if index == len(txt)-2: lstStrings.append(longestSubString)
    return max(lstStrings, key=len)
    
            
            
        
        
        



print(1,longest_nonrepeating_substring("abcabcbb") == "abc")
print(2,longest_nonrepeating_substring("aaaaaa") == "a")
print(3,longest_nonrepeating_substring("abcde") == "abcde")
print(4,longest_nonrepeating_substring("abcda") == "abcd")
print(5,longest_nonrepeating_substring("aaccddeeffb") == "ac")
print(6,longest_nonrepeating_substring("abdde") == "abd")
print(7,longest_nonrepeating_substring("ccdddcccc") == "cd")
print(8,longest_nonrepeating_substring("cdxdxccxc") == "cdx")
print(9,longest_nonrepeating_substring("abddefgh") == "defgh")
print(10,longest_nonrepeating_substring("abcdabcd") == "abcd")
print(11,longest_nonrepeating_substring("abddebcc") == "abd")
print(12,longest_nonrepeating_substring("xyxxyzyzy") == "xyz")
print(13,longest_nonrepeating_substring("kjlmjsdeee") == "lmjsde")
print(14,longest_nonrepeating_substring("kjlmjsdfew") == "lmjsdfew")
print(15,longest_nonrepeating_substring("kjlmjsdfewii") == "lmjsdfewi")
print(16,longest_nonrepeating_substring("kjlmjjiiiidfewii") == "idfew")
print(17,longest_nonrepeating_substring("kjlmjjiiiidfiwii") == "kjlm")