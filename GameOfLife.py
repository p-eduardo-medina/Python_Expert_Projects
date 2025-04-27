# A tank has pure water flowing into it at 10 l/min.
# The contents of the tank are kept thoroughly mixed, 
# and the contents flow out at 10 l/min. Salt is added 
# to the tank at a rate of 0.1 kg/min. Initially, 
# the tank contains 10 kg of salt in 100 l of water.
# Devise a function whose argument is time t. 
# The function returns the amount of salt (kg) 
# left in the tank after t minutes rounded to 3 decimal places.
def game_of_life(board):
    Rows, Columns = len(board), len(board[0])
    CountMatrix = []
    for row in range(Rows):
        CountRow = ''
        for column in range(Columns):
            count = 0
            subrows,subcolumns = [subrow for subrow in range(row-1,row+2) if subrow>=0],[subcolumn for subcolumn in range(column-1,column+2) if subcolumn>=0]
            for subrow in subrows:
                for subcolumn in subcolumns:
                    if subrow!=row or subcolumn!=column:
                        try:
                            if board[subrow][subcolumn]==1: count+=1
                        except Exception as exc: pass
            if board[row][column]==1:
                CountRow = CountRow+'I' if count == 2 or count == 3 else CountRow + '_'
            elif board[row][column]==0:
                CountRow = CountRow+'I' if count == 3 else CountRow + '_'
        CountMatrix.append(CountRow+'\n')
    return ''.join(CountMatrix)


example1 = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
]

example2 = [
  [0, 1, 0],
  [1, 1, 1],
  [0, 1, 0],
]

example3 = [
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1],
]

example4 = [
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 0],
]

glider = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
]

smallExploder = [
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0],
]

exploder = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 0],
]

rowOf10 = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

lightweightSpaceship = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 0],
  [0, 1, 0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
]

tumbler = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 1, 1, 0, 0],
  [0, 0, 1, 1, 0, 1, 1, 0, 0],
  [0, 0, 0, 1, 0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 1, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

checkerboard = [
  [1, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1, 0, 1, 0, 1],
]

bigShape = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
  [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

print(game_of_life(example1))
print('___\n___\n___')
print(game_of_life(example2),'III\nI_I\nIII')
print('\n\n\n')
print(game_of_life(example3),'___\n_I_\n___')
print('\n\n\n')
print(game_of_life(example4),'___\n_I_\n___')
print('\n\n\n')
print(game_of_life(glider),'_____\n_____\n_I_I_\n__II_\n__I__')
print('\n\n\n')
print(game_of_life(smallExploder),'_____\n_III_\n_I_I_\n_I_I_\n__I__\n_____')
print('\n\n\n')
print(game_of_life(exploder),'_______\n__I_I__\nII___II\nIII_III\nII___II\n__I_I__\n_______')
print('\n\n\n')
print(game_of_life(rowOf10),'__IIIIIIII__\n__IIIIIIII__\n__IIIIIIII__')
print('\n\n\n')
print(game_of_life(lightweightSpaceship),'___II__\n__IIII_\n__II_II\n____II_\n_______\n_______')
print('\n\n\n')
print(game_of_life(tumbler),'_________\n__II_II__\n_________\n___I_I___\n___I_I___\nII_I_I_II\n_II___II_\n_________')
print('\n\n\n')
print(game_of_life(checkerboard),'_IIIIIII_\nI_______I\nI_______I\nI_______I\nI_______I\nI_______I\n_IIIIIII_')
print('\n\n\n')
print(game_of_life(bigShape),'_________I_____\n__II____I_I____\n__II____I______\n_I__I__II__I___\n_I_II___I_I_I__\n__I________III_\n___II____I__II_\n____II_________\n_____I__I______\n_______________')