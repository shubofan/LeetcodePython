from typing import List


class Solution:

	# 时间复杂度：O(mn)。其中m、n分别为矩阵的行数和列数。 Need to mark each element in the grid
	# 空间复杂度：O(mn)。递归所需要的栈空间大小为mn。

	def closedIsland(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		res = 0

		# mark 0 to 1 from the edges. 
		for x in range(m):
			if grid[x][0] == 0:
				self.fill_connected(grid, x, 0)
			if grid[x][n - 1] == 0:
				self.fill_connected(grid, x, n - 1)
		for y in range(n):
			if grid[0][y] == 0:
				self.fill_connected(grid, 0, y)
			if grid[m - 1][y] == 0:
				self.fill_connected(grid, m - 1, y)

		# fill connected starting from 0
		for x in range(1, m - 1):
			for y in range(1, n - 1):
				if grid[x][y] == 0:
					self.fill_connected(grid, x, y)
					res += 1
		return res

	def fill_connected(self, grid, x, y):
		m, n = len(grid), len(grid[0])
		grid[x][y] = 1

		dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
		for d in dirs:
			x_next, y_next = x + d[0], y + d[1]
			if 0 < x_next < m - 1 and 0 < y_next < n - 1 and grid[x_next][y_next] == 0:
				self.fill_connected(grid, x_next, y_next)
