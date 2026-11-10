# Create a function which returns the next
# letters alphabetically in a given string.
# If the last letter is a "Z", change the z
# rest of the letters accordingly.
def next_letters(s):
    if s == "":return "A"
    AB ="abcdefghijklmnopqrstuvwxyz".upper()
    def nlett(s):
        if len(s)==0:return ""
        if s[-1]=="Z":
            if len(s)==1:return "AA"
            else:return "A"+nlett(s[:-1])
        else: return AB[(AB.index(s[-1])+1)]+s[::-1][1:]
    return nlett(s)[::-1]


TEST = [
"A",
"ABC",
"Z",
"CAZ",
"AAA",
"ZYZ",
"ZZZ",
"ACZZZ",
"ZZZAZAZAZAZAZZZZ", #######
"",
"ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
"EDABIS",
"JOSHTZ"]

ANSW = [
"B",
"ABD",
"AA",
"CBA",######
"AAB",
"ZZA",
"AAAA",
"ADAAA",
"ZZZAZAZAZAZBAAAA",######
"A",
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
"EDABIT",
"JOSHUA"]



from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()


for i, z in enumerate(ANSW): 
    p=next_letters(TEST[i])
    if p == z:
        print(f'{Fore.GREEN}Correcto!{Style.RESET_ALL}\tEl resultado de {TEST[i]} es {z}')
    else:
        print(f'{Fore.RED}No esCorrecto!{Style.RESET_ALL}\tEl resultado de {TEST[i]} no es {z}')