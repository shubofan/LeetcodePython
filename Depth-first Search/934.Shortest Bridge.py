import collections


class Solution:
	def shortestBridge(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		self.q = collections.deque()
		self.visited = set()

		# First, do a dfs. look for a square with a 1 we haven't visited, and dfs to get the component of that region -> i.e. a grid
		def dfs(grid, x, y):
			self.visited.add((x, y))
			self.q += [(x, y)]
			m, n = len(grid), len(grid[0])
			dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

			for d in dirs:
				x_next, y_next = x + d[0], y + d[1]
				if 0 <= x_next < m and 0 <= y_next < n and grid[x_next][y_next] == 1 and (
				x_next, y_next) not in self.visited:
					dfs(grid, x_next, y_next)

		found = False

		for x in range(m):
			if found:
				break
			for y in range(n):
				if grid[x][y] == 1 and not found:
					dfs(grid, x, y)
					found = True
					break

		# For all the element in the region, do bfs, until reach any node in element in another grid
		level = 0
		while self.q:
			size = len(self.q)

			while size > 0:
				x, y = self.q.popleft()
				dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
				for d in dirs:
					x_next, y_next = x + d[0], y + d[1]
					if 0 <= x_next < m and 0 <= y_next < n and (x_next, y_next) not in self.visited:
						if grid[x_next][y_next] == 1:
							return level
						elif grid[x_next][y_next] == 0:
							self.q += [(x_next, y_next)]
				size -= 1
			level += 1

		return -1