class Solution:
	"""
	@param board: a 2D integer array
	@return: the current board
	"""

	# each function call takes O(MN), at most it will (M//3)*(N//3) time
	# so total time complexity is  O (MN* M//3*N//3 ) = O(M^2N^2)

	# Space O(1) since modify board in place
	def candyCrush(self, board):
		m, n = len(board), len(board[0])

		# False if the board is stable, otherwise, need the call function again
		todo = False

		# crush Horizontally . Make val of cell to negative if need to be crushed    #  A A A
		for row in range(m):
			for col in range(n - 2):
				if abs(board[row][col]) == abs(board[row][col + 1]) == abs(board[row][col + 2]) != 0:
					board[row][col] = board[row][col + 1] = board[row][col + 2] = -abs(board[row][col])
					todo = True

		# crush vertically Make val of cell to negative if need to be crushed # A
																			  # A
																			  # A
		for row in range(m - 2):
			for col in range(n):
				if abs(board[row][col]) == abs(board[row + 1][col]) == abs(board[row + 2][col]) != 0:
					board[row][col] = board[row + 1][col] = board[row + 2][col] = -abs(board[row][col])
					todo = True

		for col in range(n):
			# re-write each col from bottom to up. Since we need to fill up with 0
			row_rewrite = m - 1
			for row in range(m - 1, -1, -1):
				if board[row][col] > 0:
					board[row_rewrite][col] = board[row][col]
					row_rewrite -= 1
			while row_rewrite >= 0:
				board[row_rewrite][col] = 0
				row_rewrite -= 1

		return self.candyCrush(board) if todo else board