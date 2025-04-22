# This challenge is a simplified version of that. 
# Write a function that takes in a tuple of unique 
# positive integers and a target positive integer 
# and returns a string containing an expression that
# combines the numbers in the tuple so that they 
# meet the target, subject to certain rules 
# explained in the notes below.
def countdown(operands, target):
    OPERATORS = {'+','-', '*', '//'}
    
    

def respectiveOperation(Operator,num1,num2):
    solution = 0
    if Operator == '+':
        solution = num1+num2
    elif Operator == '-':
        solution = num1-num2
    elif Operator == '*':
        solution = num1+num2
    elif Operator == '//':
        solution = num1/num2
    else:
        return None
    return solution
        
        



import re

def checker(answer, operands, target):
    '''
    Returns target if answer evaluates to it within the rules, otherwise
    'Failed'
    '''
    OPERATORS = {'+','-', '*', '//'}
    
    try:
        ans = eval(answer)
        assert ans == target, 'Expression does not match target'
        expr = answer.replace(' ','')
        nums = re.split('[^\d]', expr)
        assert sorted(int(num) for num in nums if num.isnumeric()) == \
               sorted(operands), 'Must use each operand once'
        ops = re.split('\d+', expr)
        assert all(op in OPERATORS for op in ops if op != ''), \
              'Must only use designated operators'

        return ans
    except AssertionError as e:
        print(e)
        return 'Failed'
				
operands = (
            (4,9,50,100),(1,2),(1,2,3,4,5),(1,10,20),(4,20,75,100),
            (4,7,9,20),(3,5,7,15,100),(2,3,5,75),(3,12),(3,4,5)
           )

targets = (554,3,7,2,345,208,687,158,4,23)

for i, nums in enumerate(operands):
    print(checker(countdown(nums,targets[i]),nums,targets[i]),targets[i])