def fractions(decimal):
    from decimal import Decimal
    from sympy import factorint
    b1 = decimal.find("(")
    b2 = decimal.find(")")
    point = decimal.find(".")
    powerB1 = len(decimal[point+1:b1])
    

    numNoRepeat,numRepet = decimal[0:b1], decimal[b1+1:b2]
    numComplete = numNoRepeat+numRepet
    numFLoatComplete = numComplete+numRepet
    powerB2 = (len(numRepet))
    newNumFLoat = numFLoatComplete[0:point]+numFLoatComplete[point+1:point+1+powerB2]+'.'+numFLoatComplete[point+1+powerB2:]
    
    
    diff = Decimal(newNumFLoat)-Decimal(numComplete)
    Numerator = int(round(diff*10**powerB1))
    Denominator = (10**(powerB2)-1)*10**powerB1


    FNumerator = factorint(Numerator)
    FDenominator = factorint(Denominator)


    for key in FNumerator.keys():
        if key in FDenominator.keys():
            rest = 0
            if FNumerator[key]<FDenominator[key]:
                rest = FNumerator[key]
            else:
                rest = FDenominator[key]
            FDenominator[key]-=rest
            FNumerator[key]-=rest
    Numerator,Denominator=1,1
    for base,power in FNumerator.items():
        Numerator*=base**power
    for base,power in FDenominator.items():
        Denominator*=base**power
      
    return str(Numerator)+"/"+str(Denominator)


     

print(f'\n\nThe Fraction is: 0.(6) || The calculate solution is: {fractions("0.(6)")} ||  The expected solution is ➞ "2/3"')
print(f'\n\nThe Fraction is: 1.(1) || The calculate solution is: {fractions("1.(1)")} ||  The expected solution is ➞ "10/9"')
print(f'\n\nThe Fraction is: 3.(142857) || The calculate solution is: {fractions("3.(142857)")} ||  The expected solution is ➞ "22/7"')
print(f'\n\nThe Fraction is: 0.19(2367) || The calculate solution is: {fractions("0.19(2367)")} ||  The expected solution is ➞ "5343/27775"')
print(f'\n\nThe Fraction is: 0.1097(3) || The calculate solution is: {fractions("0.1097(3)")} ||  The expected solution is ➞ "823/7500"')
print(f'\n\nThe Fraction is: 0.(052631578947368421) || The calculate solution is: {fractions("0.(052631578947368421)")} ||  The expected solution is ➞ "1/19"')