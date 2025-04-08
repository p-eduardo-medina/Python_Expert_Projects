"""Tap code is a way to communicate messages via
a series of taps (or knocks) for each letter in the message.
Letters are arranged in a 5x5 polybius square, 
with the letter "K" being moved to the space with "C"."""
def tap_code(text):
    dictPolu = getPolyBus('c','k')
    response = ''
    if text[0]!='.':
        for char in text:
            response+= '.'*dictPolu[char][0] + ' '+ '.'*dictPolu[char][1]+' '
        response = response[:len(response)-1]
    else:
        listOfSpaces = [i for i in range(len(text)) if text[i] !='.']
        listOfSpaces = [Num for i,Num in enumerate(listOfSpaces) if i%2!=0]
        listOfSpaces.insert(0, -1)
        listOfSpaces.append(len(text))
        for Index in range(len(listOfSpaces)-1):
            lstPoints = text[listOfSpaces[Index]+1:listOfSpaces[Index+1]].split(' ')
            lstPoints = [len(strPoint) for strPoint in lstPoints]
            for key,coords in dictPolu.items():
                if coords == lstPoints:
                    response += key
                    break
    return response


def getPolyBus(char0, char1):
    dictPolyBus={}
    import string
    lowercase_alphabet = string.ascii_lowercase
    for i in range(5):
        for j in range(5):
            if lowercase_alphabet[0] != char1:
                dictPolyBus[lowercase_alphabet[0]] = [i+1,j+1]
                lowercase_alphabet= lowercase_alphabet[1:len(lowercase_alphabet)]
            else:
                dictPolyBus[lowercase_alphabet[0]] = dictPolyBus[char0]
                dictPolyBus[lowercase_alphabet[1]] = [i+1,j+1]
                lowercase_alphabet = lowercase_alphabet[2:len(lowercase_alphabet)]
    return dictPolyBus





print(tap_code("greeting")== ".. .. .... .. . ..... . ..... .... .... .. .... ... ... .. ..")
print(tap_code("confrontation")== ". ... ... .... ... ... .. . .... .. ... .... ... ... .... .... . . .... .... .. .... ... .... ... ...")
print(tap_code("leadership")== "... . . ..... . . . .... . ..... .... .. .... ... .. ... .. .... ... .....")
print(tap_code("ankle")== ". . ... ... . ... ... . . .....")
print(tap_code("extreme")== ". ..... ..... ... .... .... .... .. . ..... ... .. . .....")
print(tap_code(".... .... ... .... ... ... .. .... .. .. .. ... .... ....")=="tonight")
print(tap_code("... . ... .... ..... .... . . ... . .... .... ..... ....")== "loyalty")
print(tap_code(".... .. . ..... .. . . ..... .... .. .... .. . . ... .")=="referral")
print(tap_code(". ..... ..... ... ... ..... .... .. . ..... .... ... .... ... .. .... ... .... ... ...")=="expression")
print(tap_code(". . .. . .. . .. .... ... ... .. .... .... .... ..... ....")== "affinity")
print(tap_code("correspondence")== ". ... ... .... .... .. .... .. . ..... .... ... ... ..... ... .... ... ... . .... . ..... ... ... . ... . .....")
print(tap_code("atmosphere")==". . .... .... ... .. ... .... .... ... ... ..... .. ... . ..... .... .. . .....")
print(tap_code("absolute")== ". . . .. .... ... ... .... ... . .... ..... .... .... . .....")
print(tap_code("redundancy")== ".... .. . ..... . .... .... ..... ... ... . .... . . ... ... . ... ..... ....")
print(tap_code("infrastructure")== ".. .... ... ... .. . .... .. . . .... ... .... .... .... .. .... ..... . ... .... .... .... ..... .... .. . .....")
print(tap_code("... ..... ... .... .. .... ... ... .... ....")== "point")
print(tap_code("... ..... .... .. . ..... .. . . ..... .... .. . ..... ... ... . ... . .....")=="preference")
print(tap_code(".. .. .... ..... .. .... . .... . .....")=="guide")
print(tap_code(". ... .. ... . . .... .. . . . ... .... .... . ..... .... .. .. .... .... ... .... .... .. .... . ...")=="characteristic")
print(tap_code(". ... ... .... ... .. ... .. . ..... .... .. . ... . .....")=="commerce")