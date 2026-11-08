from itertools import groupby  as gb
def is_sorted2(words, alphabet):
    count =0
    while len(words)>1 or len(set(words))>1:
        x = [alphabet.index(w[count]) if count<len(w) else -1 for w in words]
        if x != sorted(x): return False
        else: 
            if len(x) == len(set(x)):return True
            else: 
                lstErr = {x.index(k) for k, v in gb(x) if len(list(v)) == 1}
                words = [word for i, word in enumerate(words) if i not in lstErr]
                count += 1
    return True

def is_sorted(words, alphabet):
    d = {c: i for i, c in enumerate(alphabet)}
    return words == sorted(words, key=lambda palabra: [d[letra] for letra in palabra])
        
    


print(f'{is_sorted(["hello", "edabitlot"], "hlabcdefgijkmnopqrstuvwxyz") }__➞__True')
print(f'{is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") }__➞__ False')
print(f'{is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") }➞ False')
print(f'{is_sorted(["deceased", "folks", "can", "vote"], "abdefghijklmnopqrstcuvwxyz")}➞ True')
print(f'{is_sorted(['ornggrqho', 'qjcbnhnax', 'bamnch', 'sujmxeu', 'szjoxirq', 'luvgiu', 'tkramy', 'vhi', 'ahjl', 'dpm'], "xiujyowcqbkslgrhzftnmvadep")}, True')