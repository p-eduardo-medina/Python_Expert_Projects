def ecg_seq_index(n):
    SEQUENCE,i = [1,2],0
    if n in SEQUENCE: return SEQUENCE.index(n)  
    while True:
        i+=1    
        if not i in SEQUENCE:
            Ifactors = Factors(i)
            Efactor = Factors(SEQUENCE[-1])
            for efactor in Efactor:
                if efactor in Ifactors:
                    SEQUENCE.append(i)  
                    if n in SEQUENCE:return SEQUENCE.index(n)  
                    i = 0                  
                    break                
def Factors(n):
    listFctors = {}
    i = 2
    while i*i<=n:
        if n%i==0:
            n/=i
            if i in listFctors.keys():
                listFctors[int(i)]+=1
            else:
                listFctors[int(i)]=1
        else:
            i+=1
    if n>1:
        if int(n) in listFctors.keys():
                listFctors[int(n)]+=1
        else:
            listFctors[int(n)]=1
    return list(listFctors.keys())

#print(f'Input: 3 || Calculate solution ➞ {ecg_seq_index(3)} || Expected solution ➞ 4')
#print(f'Input: 5 || Calculate solution ➞ {ecg_seq_index(5)} || Expected solution ➞ 9')
#print(f'Input: 7 || Calculate solution ➞ {ecg_seq_index(7)} || Expected solution ➞ 13')

for i in range(1,61):
    print(f'El valor {i} está en la posición {ecg_seq_index(i)}.')


