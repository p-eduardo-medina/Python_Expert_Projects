def who_goes_free(n, k):
    ppl = [x for x in range(n)]
    index = 0
    while len(ppl)>1:
        index = (index + k -1)%len(ppl)
        ppl.pop(index)
    return ppl[0]


who_goes_free(9, 2)