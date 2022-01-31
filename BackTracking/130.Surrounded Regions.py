class Solution:
	def solve(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		m, n = len(board), len(board[0])

		def dfs(board, x, y):
			m, n = len(board), len(board[0])

			board[x][y] = 'M'
			dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
			for d in dirs:
				x_next, y_next = x + d[0], y + d[1]
				if 0 <= x_next < m and 0 <= y_next < n and board[x_next][y_next] == 'O':
					dfs(board, x_next, y_next)

		# search from boarder, marked cell to "M"
		for i in range(m):
			for j in range(n):
				if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
					dfs(board, i, j)
		# M is not flipped
		for i in range(m):
			for j in range(n):
				if board[i][j] == 'M':
					board[i][j] = 'O'
				elif board[i][j] == 'O':
					board[i][j] = 'X'