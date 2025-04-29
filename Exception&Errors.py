#Errors and Exceptions

x = 1
if x <0:
    raise Exception('X debería ser positivo')
a=1
assert(a>=0),'X no es positivo'

try:
    a = 5/0    
except Exception as e:
    print(e)
    
try:
    a = 5/1
    b = a+'1'    
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything is fine')
finally:
    print('Cleaning up...')
    
print('\n\t Hello World')

### Los class y la función son el paquete del error
class ValueTooHightError(Exception):
    pass 
class ValueTooSmall(Exception):
    def __init__(self, message,value):
        self.message = message
        self.value = value        
def test_value(x):
    if x >100:
        raise ValueTooHightError('El valor es demasiado grande :v')
    if x<5:
        raise ValueTooSmall('Valor demasiado pequeño',x)
### Los class y la función son el paquete del error
    
    
try:
    test_value(2)
except ValueTooHightError as e:
    print(e)
except ValueTooSmall as e:
    print(e.message, e.value)
finally:
    print(':D')
    
