def newton_raphson(c):
    dictPol = {}
    for i,num in enumerate(c[::-1]): dictPol[i]=num*10
    dictDiffPol ={}
    for power,base in dictPol.items():
        if power>0: dictDiffPol[power-1] = base*power
    x_i, x_ip1 = 0.0,0.0
    while True:
        if abs(evalPol(dictPol.values(),x_i))<0.001: return round(x_i,3)
        x_ip1 = x_i - ( evalPol(dictPol.values(),x_i) / evalPol(dictDiffPol.values(),x_i) )
        x_i = x_ip1
def evalPol(Pol,base):
    value = 0
    for i,Coef in enumerate(Pol): value += Coef*(base**i)
    return value

#[1,  x,  x**2,  x**3,   ....]
print(f'{newton_raphson([0.0, -0.1, -0.2, 0.3])}/1.0') #  -0.1x -0.2x**2 =0.3x**2
print(f'{newton_raphson([-1.4, -0.9, -1.0, 5.2])}/1.23')
print(f'{newton_raphson([2.4, 0.1, -4.6, 8.2])}/-1.939')
print(f'{newton_raphson([0.0, 0.0, -1.0, 2.0])}/2.0')
print(f'{newton_raphson([-0.4, 3.8, 0.7, -5.5])}/9.532')