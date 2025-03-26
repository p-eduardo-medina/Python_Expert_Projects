def freq_count(lst, el):
    var = freqCountAux(lst,el,0,{})    
    result = []
    for key,value in var.items():
        result.append([key,value])
    result = sorted(result,key = lambda x:x[0])
    return result

def freqCountAux(lst,el,nesting,dictNesting):
    for element in lst:
        if type(element)!=list:
            if element==el:
                if nesting in dictNesting.keys():
                    dictNesting[nesting]+=1
                else:
                    dictNesting[nesting]=1
        else:
            newDict =  freqCountAux(element,el,nesting+1,dictNesting)
            dictNesting = newDict
    if not(nesting in dictNesting.keys()):
        dictNesting[nesting] = 0        
    return dictNesting


print(f'\n\nEl calculo es: {freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)} \nLa solucion es ➞ [[0, 1], [1, 2], [2, 3]]')
print(f'\n\nEl calculo es: {freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)} \nLa solucion es ➞ [[0, 3], [1, 4], [2, 0]]')
print(f'\n\nEl calculo es: {freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)}\nLa soluciòn es ➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]')