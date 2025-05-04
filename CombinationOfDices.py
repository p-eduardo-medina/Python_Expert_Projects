""" Las Vegas style dice have 6 sides numbered 1 to 6. When rolling 2 dice,
a six is 5 times more likely than a two because a six can be rolled 5 different
ways (1 + 5, 5 + 1, 2 + 4, 4 + 2, 3 + 3), while a two can only be rolled 1 way (1 + 1).
Create a function that accepts two arguments:the number of dice rolled,
and the outcome of the roll. The function returns the number of possible 
combinations that could produce that outcome. The number of dice can vary from 1 to 6.
 """
import itertools
def dice_roll(n, outcome):
    Ks = [0,1,2,3,4,5,6]
    Combinations = Ks*n
    
        
    


print(dice_roll(1, 6), 1)
print(dice_roll(2, 2), 1)
print(dice_roll(2, 9), 4)
print(dice_roll(3, 7), 15) 
print(dice_roll(3, 18), 1)
print(dice_roll(4, 11), 104)
print(dice_roll(4, 21), 20)
print(dice_roll(5, 6), 5)
print(dice_roll(5, 26), 70)
print(dice_roll(6, 6), 1)
print(dice_roll(6, 21), 4332)
print(dice_roll(6, 31), 252)
