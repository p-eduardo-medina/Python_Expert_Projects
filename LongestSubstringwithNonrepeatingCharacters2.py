# Write a function that returns the 
# longest non-repeating substring for a string input.
def longest_nonrepeating_substring(txt):
    lstStrings = []
    longestSubString = txt[0]
    for index,char in enumerate(txt[1:len(txt)]):
        if char not in longestSubString:
            longestSubString+=char
        else:
            lstStrings.append(longestSubString)
            longestSubString = char
        if index == len(txt)-2: lstStrings.append(longestSubString)
    for index,char  in enumerate(lstStrings[:len(lstStrings)-1]):
        strTest = lstStrings[index]+lstStrings[index+1]
        if strTest[0] not in strTest[1:len(strTest)]:
            lstStrings.append(strTest)
    return max(lstStrings, key=len)
            



print(0 ,longest_nonrepeating_substring("abcabcbb") == "abc")
print( 1,longest_nonrepeating_substring("aaaaaa") == "a")
print( 2,longest_nonrepeating_substring("abcde") == "abcde")
print(3 ,longest_nonrepeating_substring("abcda") == "abcd")
print( 4,longest_nonrepeating_substring("aaccddeeffb") == "ac")
print(5 ,longest_nonrepeating_substring("abdde") == "abd")
print(6 ,longest_nonrepeating_substring("ccdddcccc") == "cd")
print(7 ,longest_nonrepeating_substring("cdxdxccxc") == "cdx")
print(8 ,longest_nonrepeating_substring("abddefgh") == "defgh")
print(9 ,longest_nonrepeating_substring("abcdabcd") == "abcd")
print(10 ,longest_nonrepeating_substring("abddebcc") == "debc")
print(11 ,longest_nonrepeating_substring("xyxxyzyzy") == "xyz")
print(12 ,longest_nonrepeating_substring("kjlmjsdeee") == "lmjsde")
print(13 ,longest_nonrepeating_substring("kjlmjsdfew") == "lmjsdfew")
print(14 ,longest_nonrepeating_substring("kjlmjsdfewii") == "lmjsdfewi")
print( 15,longest_nonrepeating_substring("kjlmjjiiiidfewii") == "idfew")
print( 16,longest_nonrepeating_substring("kjlmjjiiiidfiwii") == "kjlm")