# An English text needs to be encrypted using 
# Edabit’s encryption scheme. First, the spaces 
# are removed from the text. Let L be the length 
# of this text. Then, characters are written into 
# a grid, whose rows and columns have the 
# following constraints:
# For example, the sentence "if man was meant 
# to stay on the ground god would have given us 
# roots", after removing spaces, is 54 characters long.
# The square root of 54 is between 7 and 8, so 
# it is written in the form of a grid with 7 rows and 8 columns.
import math
def encryption(txt):
    txt = txt.replace(' ','')
    txtLenght = len(txt)
    rootLength = round(math.sqrt(txtLenght))
    minArea = math.inf
    RC = []
    for index in range(rootLength,rootLength+2):
        if rootLength*(index)>=txtLenght and rootLength*(index)<minArea:
            RC = [rootLength,index]
            minArea = rootLength*(index)
    gridText = []
    for row in range(RC[0]):
        rowString = []
        for column in range(RC[1]):
            if row*RC[1]+column>txtLenght-1: rowString.append('')
            else: rowString.append( txt[row*RC[1]+column] ) 
        gridText.append(rowString)  
    gridSolution = []
    for indexcolum in range(len(gridText[0])): gridSolution.append(''.join([gridText[indexrow][indexcolum] for indexrow in range(len(gridText))]))
    return ' '.join(gridSolution)


print(encryption('if man was meant to stay on the ground god would have given us roots')=='imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau')
print(encryption("haveaniceday") == "hae and via ecy")
print(encryption("feedthedog") == "fto ehg ee dd")
print(encryption("chillout") == "clu hlt io")
print(encryption("A Fool and His Money Are Soon Parted.") == "Anoea FdnSr oHeot oiyoe lsAnd aMrP.")
print(encryption("One should not worry over things that have already happened and that cannot be changed.") == "Onvtlphb. noehreae etraentc swttaech hohhddaa oriayann urnvhnng lygeadoe dosapttd")
print(encryption("Back to Square One is a popular saying that means a person has to start over, similar to: back to the drawing board.") == "Brpgatroea aeutpo,:dr cOlhessbrd knaartiaa. tertsamcw oismoriki Ssaentltn qayahoaog upinavrtb aonssetho")