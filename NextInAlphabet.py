# Create a function which returns the next
# letters alphabetically in a given string.
# If the last letter is a "Z", change the 
# rest of the letters accordingly.
def next_letters(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if s != '':
        if s[len(s)-1]!='Z': s = s[:len(z)-1] + alphabet[alphabet.find(s[len(z)-1])+1]
        else:
            count = 1
            while True:
                if s[len(s)-count] == 'Z' and len(s)-count>0:
                    count +=1
                else:
                    for i in range(count,0,-1):
                        if len(s)-i <1:s = 'A' + s
                        newChar = alphabet[alphabet.find(s[len(z)-i])+1] if alphabet.find(s[len(z)-i]) != len(alphabet)-1 else alphabet[0]
                        s = s[:len(s)-i]+newChar+s[len(s)-i+1:]
                    break    
    else:
        return 'A'
    return s



TEST = [
"A",
"ABC",
"Z",
"CAZ",
"AAA",
"ZYZ",
"ZZZ",
"ACZZZ",
"ZZZAZAZAZAZAZZZZ",
"",
"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
"EDABIS",
"JOSHTZ"]

ANSW = [
"B",
"ABD",
"AA",
"CBA",
"AAB",
"ZZA",
"AAAA",
"ADAAA",
"ZZZAZAZAZAZBAAAA",
"A",
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
"EDABIT",
"JOSHUA"]



from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()


for i, z in enumerate(ANSW): 
    if next_letters(TEST[i]) == z:
        print(f'{Fore.GREEN}Correcto!{Style.RESET_ALL}\tEl resultado de {TEST[i]} es {z}')
    else:
        print(f'El resultado de {TEST[i]} {Fore.RED}NO ES correcto!{Style.RESET_ALL}, {next_letters(TEST[i])} != {ANSW[i]}')