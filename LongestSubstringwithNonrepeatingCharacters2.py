# Write a function that returns the 
# longest non-repeating substring for a string input.
def longest_nonrepeating_substring(txt):
    dictPositions = dict()
    for char in txt:
        if char not in dictPositions.keys():
            Positions = [i for i in range(len(txt)) if txt[i] == char]
            dictPositions[char] = Positions
    print(dictPositions)
        
    return None
            



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