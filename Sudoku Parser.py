import re
class Sudoku:
	def __init__(self, txt):
		self.board = [list(map(int, i)) for i in re.findall('\d{9}', txt)]
	def get_row(self, n):
		return self.board[n]		
	def get_col(self, n):
		return [self.board[i][n] for i in range(9)]		
	def get_sqr(self, n, m=None):
		if m is not None: n = n//3*3 + m//3
		return [self.board[r][c] for r in range(n//3*3, n//3*3+3) for c in range(n%3*3, n%3*3+3)]     

game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

print(game.board())
#[
#  [4, 1, 7, 9, 5, 0, 0, 3, 0],
#  [0, 0, 0, 0, 0, 0, 7, 0, 0],
#  [0, 6, 0, 0, 0, 7, 0, 0, 0],
#  [0, 5, 0, 0, 0, 9, 1, 0, 6],
#  [8, 0, 0, 6, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 3, 4, 0, 0],
#  [9, 0, 0, 0, 0, 5, 0, 0, 0],
#  [0, 0, 0, 4, 3, 0, 0, 0, 0],
#  [2, 0, 0, 7, 0, 1, 5, 8, 0]
#]
#
print(game.get_row(0) )#➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
print(game.get_col(8) )##➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
print(game.get_sqr(1) )#➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
print(game.get_sqr(1, 8))# ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
print(game.get_sqr(8, 3))#➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]