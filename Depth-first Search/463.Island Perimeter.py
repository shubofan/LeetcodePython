class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		res = 0
		for x in range(m):
			for y in range(n):
				if grid[x][y] == 1:
					nbrs = self.numOfNbrs(grid, x, y)

					res += 4 - nbrs
		return res

	def numOfNbrs(self, grid, x, y):
		m, n = len(grid), len(grid[0])
		nbrs = 0

		dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

		for d in dirs:
			x_n, y_n = x + d[0], y + d[1]
			if 0 <= x_n < m and 0 <= y_n < n:

				if grid[x_n][y_n] == 1:
					nbrs += 1
		return nbrs
