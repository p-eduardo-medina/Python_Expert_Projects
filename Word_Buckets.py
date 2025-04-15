def split_into_buckets(phrase, n):
    if not any(len(ele) < n for ele in phrase.split(' ')): 
        if not all(len(nele)==n for nele in phrase.split(' ')): return []
    Words =[]
    word = ''
    i = 0
    while True:
        if i<len(phrase)-1:
            if not(len(word)<1 and phrase[i]==' '):
                word += phrase[i]
            if len(word)==n:
                if phrase[i+1]==' ':
                    Words.append(word)
                elif ' ' in word:                    
                    if phrase[i]!=' ':
                        back = word.rfind(' ')
                        if back != n-1:
                            Words.append(word[:back])
                            i -= len(word) - back -1
                        else:
                            Words.append(word[:len(word)-1])
                    else:
                        Words.append(word[:len(word)-1])
                word = ''                       
        else:
            Words.append(word+phrase[i])
            break
        i+=1                 
    return Words
        
print(split_into_buckets("she sells sea shells by the sea", 2)) #➞ []
print(split_into_buckets("she sells sea shells by the sea", 10)) #➞ ["she sells", "sea shells", "by the sea"]
print(split_into_buckets("the mouse jumped over the cheese", 7)) #➞ ["the", "mouse", "jumped", "over", "the", "cheese"]
print(split_into_buckets("fairy dust coated the air", 20) )#➞ ["fairy dust coated", "the air"]
print(split_into_buckets("a b c d e", 2) )# ["a", "b", "c", "d", "e"]
print(split_into_buckets("a b c d e", 1) )# ["a", "b", "c", "d", "e"]

print(split_into_buckets("Hola mi nombre es Pedro Eduardo Medina Gonzalez y soy Ingeniero y Físico", 15) )


