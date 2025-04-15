def findNumber(numbers):
    # Write your code here
    flag = True
    while flag:
        if len(numbers)==2:
            a = str(numbers[0]) + str(numbers[1])
            flag = False
        else:
            lista = []
            for i in range(len(numbers)-1):
                suma = numbers[i]+numbers[i+1]
                suma = suma%10
                lista.append(int(suma))
            numbers = lista        
    return a

print(findNumber([1, 2, 3, 4]))
