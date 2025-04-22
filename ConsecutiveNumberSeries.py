# Write a function that will return True
# if a given string (divided and grouped into a size)
# will contain a set of consecutive numbers
# (regardless of orientation: whether ascending or descending),
# otherwise, return False.

def is_consecutive(s):
    for length in range(1,len(s)):
        lstNum = []
        countNum = ''
        for index in range(len(s)):
            countNum+=s[index]
            if len(countNum) == length or index==len(s)-1:
                lstNum.append(int(countNum))
                countNum = ''
        flagAsce, flagDesc = all(lstNum[i]==lstNum[i+1]-1 for i in range(len(lstNum)-1)), all(lstNum[i]==lstNum[i+1]+1 for i in range(len(lstNum)-1))
        if flagAsce or flagDesc: return True
    return False
            
            
            
            
        
            
        

actual_param = [
  "121314151617", "123124125", "667666", "23242526", "444445", "1234567", "123412351236",
  "57585960616263", "500001500002500003", "919920921", "12341235123612371238",
  "326325324323",
  "54321", "56555453", "32332432536","2324256","1235", "121316", "12131213", "90090190290",
  "35236237238", "999897959493", "171615141312119", "1716171819181920", "273274273274"
]
expected = [
  True, True, True, True, True, True, True, True, True, True, True, True, True, True,
  False, False, False, False, False, False, False, False, False, False, False
]
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()


print(f"This is {Fore.GREEN}color{Style.RESET_ALL}!")
for i, z in enumerate(actual_param): 
    if is_consecutive(z) == expected[i]:
        print(f'El número {z} {Fore.GREEN}ES consecutivo{Style.RESET_ALL}!')
    else:
        print(f'El número {z} {Fore.RED}NO ES consecutivo{Style.RESET_ALL}!')
        