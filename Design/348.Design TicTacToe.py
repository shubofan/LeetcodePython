# O(N)
class TicTacToe:
	"""
	@return: nothing
	"""
	def __init__(self, n):
		self.n = n
		self.row = [0] * n
		self.col = [0] * n
		self.diagonal = 0
		self.anti_diagonal = 0


	def move(self, x, y, player):
		number = -1

		if player == 1:
			number = 1

		self.row[x] = number
		self.col[y] = number

		if x == y:
			self.diagonal += number
		if y == self.n - 1 - x:
			self.anti_diagonal += number
		if abs(sum(self.row)) == self.n or abs(sum(self.col)) or abs(sum(self.diagonal)) == self.n or abs(
				sum(self.anti_diagonal)) == self.n:
			return player
		return 0


class TicTacToe(object):

	def __init__(self, n):
		"""
		Initialize your data structure here.
		:type n: int
		"""
		self.board = [[None] * n for _ in range(n)]

	def move(self, row, col, player):
		"""
		Player {player} makes a move at ({row}, {col}).
		@param row The row of the board.
		@param col The column of the board.
		@param player The player, can be either 1 or 2.
		@return The current winning condition, can be either:
				0: No one wins.
				1: Player 1 wins.
				2: Player 2 wins.
		:type row: int
		:type col: int
		:type player: int
		:rtype: int
		"""

		if player == 1:
			self.board[row][col] = 'X'
		else:
			self.board[row][col] = 'O'

		if self.gameOver(row, col, player, len(self.board)):
			return player
		else:
			return 0

	# check if game over after play move (row, col)
	def gameOver(self, row, col, player, n):
		winCondition = 'X' if player == 1 else 'O'

		# Check vertical
		vertical = True
		for i in range(n):
			if self.board[i][col] != winCondition:
				vertical = False
				break
		if vertical:
			return True

		# Check horizontal
		horizontal = True
		for i in range(n):
			if self.board[row][i] != winCondition:
				horizontal = False
				break
		if horizontal:
			return True

		# Main Diagonal
		diagonal = True
		for i in range(n):
			if self.board[i][i] != winCondition:
				diagonal = False
				break
		if diagonal:
			return True

		# Opposite Diagonal
		oppositeDiagonal = True
		for i in range(n):
			if self.board[n - 1 - i][i] != winCondition:
				oppositeDiagonal = False
				break
		if oppositeDiagonal:
			return True

		return False

