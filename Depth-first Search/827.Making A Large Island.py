import collections
from typing import List
# x__|x__|___|___
# x__|x__|___|___
# ___|___|___|___
# ___|x__|x__|x__
class Solution:
	# O(N*N), each element in the matrix will be marked
	def largestIsland(self, grid: List[List[int]]) -> int:
		def dfs(grid, x, y):
			self.cnt[self.tag] += 1
			grid[x][y] = self.tag
			n = len(grid)
			dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
			for d in dirs:
				nx, ny = d[0] + x, d[1] + y
				if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != self.tag and grid[nx][ny] > 0:
					dfs(grid, nx, ny)

		res = 0
		n = len(grid)
		dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
		self.tag = 1
		self.cnt = collections.Counter()  # <tag, number of elements with this tag>

		# mark each connected component with each tag
		for x in range(n):
			for y in range(n):
				if grid[x][y] == 1:
					dfs(grid, x, y)
					self.tag += 1

		for x in range(n):
			for y in range(n):
				if grid[x][y] == 0:
					tags_seen = set()
					for d in dirs:
						nx, ny = d[0] + x, d[1] + y
						if 0 <= nx < n and 0 <= ny < n:
							tag = grid[nx][ny]
							if tag > 0:
								tags_seen.add(tag)
					res = max(res, sum(self.cnt[tag] for tag in tags_seen) + 1)

		return res if res != 0 else n * n