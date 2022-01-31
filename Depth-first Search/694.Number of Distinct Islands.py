class Solution:
	"""
	@param grid: a list of lists of integers
	@return: return an integer, denote the number of distinct islands
	"""

	def numberofDistinctIslands(self, grid):

		# use path to record relative path for each island
		def dfs(grid, marker, x, y, start_x, start_y, path):
			path.add((str(x - start_x) + str(y - start_y)))
			dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
			m, n = len(grid), len(grid[0])
			grid[x][y] = marker
			for d in dirs:
				nx, ny = x + d[0], y + d[1]
				if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
					dfs(grid, marker, nx, ny, start_x, start_y, path)
			return tuple(path)  # Make it tuple so it can be put to set

		m, n = len(grid), len(grid[0])
		pathSet = set()
		marker = 2

		for x in range(m):
			for y in range(n):
				if grid[x][y] == 1:
					pathSet.add(dfs(grid, marker, x, y, x, y, set()))
					marker += 1
		return len(pathSet)