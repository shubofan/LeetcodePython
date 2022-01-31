class Solution:
	def countServers(self, grid: List[List[int]]) -> int:
		def dfs(grid, x, y):
			m, n = len(grid), len(grid[0])
			grid[x][y] = 0
			self.count += 1
			for i in range(n):
				if grid[x][i] == 1:
					dfs(grid, x, i)

			for i in range(m):
				if grid[i][y] == 1:
					dfs(grid, i, y)

		m, n = len(grid), len(grid[0])

		res = 0
		for x in range(m):
			for y in range(n):
				if grid[x][y] == 1:
					self.count = 0
					dfs(grid, x, y)
					if self.count > 1:
						res += self.count

		return res