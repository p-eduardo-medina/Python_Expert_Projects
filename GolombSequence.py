""" The Golomb sequence is uniquely defined by the following rules:
    All terms are positive integers.
    No term is smaller than any previous term.
    The nth term is equal to the total number of times that the integer n appears within the sequence.
    Write a function that returns the first n terms of the Golomb sequence as a list.
 """
def golomb(n):
    lstGolomb = [2]
    while len(lstGolomb)<n:
        lstGolomb = unsqueezeList([[index+2]*(lstGolomb[index]) for index in range(len(lstGolomb))])
    lstGolomb = [1]+lstGolomb
    return lstGolomb[:n]

def unsqueezeList(lists):
    listSolvedm = []
    for lst in lists:
        listSolvedm+=lst
    return listSolvedm
 
print(golomb(1) ==[1])
print(golomb(8) ==[1, 2, 2, 3, 3, 4, 4, 4])
for i in range(1,20):
    print(golomb(i))