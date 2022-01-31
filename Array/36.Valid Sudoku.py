from typing import List


class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		def check_lst(row):
			num = set()
			for i in row:
				if i != '.':
					if i in num:
						return False
					num.add(i)
			return True

		def check_square(board, x, y):
			num = set()
			for i in range(x, x + 3):
				for j in range(y, y + 3):
					if board[i][j] != '.':
						if board[i][j] in num:
							return False
						num.add(board[i][j])
			return True

		n = len(board)

		for i in range(n):
			row = board[i]
			col = [board[j][i] for j in range(n)]
			if not check_lst(row) or not check_lst(col):
				return False

		for i in range(0, n, 3):
			for j in range(0, n, 3):
				if not check_square(board, i, j):
					return False

		return True