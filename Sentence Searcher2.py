def sentence_searcher(txt, n):
    splitSntnc, lenWords = txt.split('. '), len( txt.split( ) )
    lstCount = [ len(lst.split(' ')) for lst in splitSntnc ]
    indx = next( (i for i in range(len(lstCount)) if sum(lstCount[:i+1]) > (n + lenWords )%lenWords ) , None)
    return  splitSntnc[indx] if indx==len(lstCount)-1 else splitSntnc[indx]+'.'    



txt = "I have a dog. I have a log. There is no stopping me now."

print(f'{sentence_searcher(txt, 2)} ➞ I have a dog. ')
print(f'{sentence_searcher(txt, 4)} ➞ I have a log. ')
print(f'{sentence_searcher(txt, -1)} ➞ There is no stopping me now. ')