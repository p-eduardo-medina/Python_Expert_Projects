def minesweeper_numbers(board):
    if board == [[]]:
        return []
    NewBoard = []
    Rows = len(board)
    Columns = len(board[0])
    for i in range(Rows):
        row = []
        for j in range(Columns):
            row.append(0)
        NewBoard.append(row)    
    for i in range(Rows):
        for j in range(Columns):
            if board[i][j]==1:
                NewBoard[i][j]=9
            else:
                for ni in [i-1,i,i+1]:
                    for nj in [j-1,j,j+1]:
                        if (not( ni == i and nj == j )):
                            if ni>=0 and nj>=0 and ni<Rows and nj< Columns:
                                NewBoard[i][j] += board[ni][nj]
                                                 
    return NewBoard


print(minesweeper_numbers([
 [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 1, 0, 0]
]
))