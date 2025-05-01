# Create a function that takes in two positive integers 
# start and n and returns a list of the first n terms 
# of the look-and-say sequence starting at the given start.
# Each term of the look-and-say sequence (except for 
# the first term) is created from the previous term 
# using the following process.

def look_and_say(start, n):
    lstFirstNTerms = [start]
    for index in range(n-1):
        numStr = str(lstFirstNTerms[len(lstFirstNTerms)-1])
        auxLstStr,auxStr = [],''
        for indexC,char in enumerate(numStr): 
            try:
                auxStr+=char
                if not char == numStr[indexC+1]:
                    auxLstStr.append(str(len(auxStr)) + auxStr[0])
                    auxStr=''
            except: auxLstStr.append(str(len(auxStr)) + auxStr[0])  
        lstFirstNTerms.append(int(''.join(auxLstStr)))
    return lstFirstNTerms

tests = [
	((1, 7), [1, 11, 21, 1211, 111221, 312211, 13112221]),
	((123, 4), [123, 111213, 31121113, 1321123113]),
	((70, 5),  [70, 1710, 11171110, 31173110, 132117132110]),
	((111312211, 2),  [111312211, 3113112221]),
	((2, 10), [2, 12, 1112, 3112, 132112, 1113122112, 311311222112, 13211321322112, 1113122113121113222112, 31131122211311123113322112]),
	((144, 4), [144, 1124, 211214, 1221121114]),
	((11111111, 3), [11111111, 81, 1811]),
	((0, 4), [0, 10, 1110, 3110]),
]

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

for test in tests:
    print("\nInput: " + str(test[0]))
    if look_and_say(*test[0]) == test[1] : 
        print(f"{test[1]}\nThis is {Fore.GREEN}Correct{Style.RESET_ALL}!")
    else: 
        print(f"This is {Fore.RED}Incorrect{Style.RESET_ALL}!")
        