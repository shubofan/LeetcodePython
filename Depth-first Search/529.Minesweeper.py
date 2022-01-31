from typing import List


class Solution:
	def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
		# (x,y) = M -> (x, y) = X
		# (x,y) = E -> all adjacent mines unrevealed, (x,y) = B
		# (x,y) = E -> at least 1 adjacent mine revealed, (x,y) = digit

		x, y = click[0], click[1]

		if board[x][y] == 'M':
			board[x][y] = 'X'
		elif board[x][y] == 'E':
			self.reveal(board, x, y)
		return board

	def reveal(self, board: List[List[str]], x: int, y: int) -> None:
		m, n = len(board), len(board[0])
		# (x,y) not in board or board[x][y] != E
		if x >= m or x < 0 or y >= n or y < 0 or board[x][y] != 'E':
			return
		directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
		num_of_adjacent_mines = 0
		for d in directions:
			x_next, y_next = x + d[0], y + d[1]
			if 0 <= x_next < m and 0 <= y_next < n and board[x_next][y_next] == 'M':
				num_of_adjacent_mines += 1
		# at least 1 adjacent mine revealed, (x,y) = digit
		if num_of_adjacent_mines > 0:

			board[x][y] = str(num_of_adjacent_mines)
		#  all adjacent unrevealed, (x,y) = B and reveal all its neighbours
		else:
			board[x][y] = 'B'
			for d in directions:
				x_next, y_next = x + d[0], y + d[1]
				self.reveal(board, x_next, y_next)
