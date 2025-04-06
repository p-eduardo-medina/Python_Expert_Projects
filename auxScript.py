
a = [1,2,3]

for i in range(5):
    try:
        print(a[i])
    except Exception as e:
        print(f'Exeption: {e}')
        a.append(i+1)
print(a)


class NewExeptionLalo(Exception):
    def __init__(self,message, value):
        self.message = message
        self.value = value
class NewExceptionLAlo2(Exception):
    def __init__(self, message, value):
        self.messagge = message
        self.value = value
def testValue(Num):
    if Num > 100:
        raise NewExeptionLalo('Valor DEmasiado Grande', Num)
    elif Num<0:
        raise NewExceptionLAlo2(message = 'Valor muy bajo',value = Num)
    
try:
    testValue(-1)
except NewExeptionLalo as NEL:
    print(NEL)
except NewExceptionLAlo2 as NEL2:
    print(NEL2)
finally:
    print('Fin del proceso')

a = [2,4,6,8,0]
try:
    c =  [x-1 for x in a if x>0]
except Exception as Exc:
    print(f'Error: {Exc}')
print(f'Vector c = {c}')
