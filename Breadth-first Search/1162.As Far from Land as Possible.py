import collections
from typing import List


class Solution:
	# First each land(i.e. 1), do a bfs, to cover all waters level by level
	# To find the max level
	def maxDistance(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

		seen = set()
		q = collections.deque()

		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					q.append((i, j))
					seen.add((i, j))
		# all waters, all lands, return -1
		if not q or len(q) == m * n:
			return -1

		level = -1
		while q:
			level += 1
			size = len(q)
			for i in range(size):
				x, y = q.popleft()
				for dd in dirs:
					x_next, y_next = x + dd[0], y + dd[1]
					if 0 <= x_next < m and 0 <= y_next < n and grid[x_next][y_next] == 0 and (x_next, y_next) not in seen:
						seen.add((x_next, y_next))
						q.append((x_next, y_next))
		return level


class Solution:
	# First each land(i.e. 1), do a bfs, to cover all waters level by level
	# To find the max level
	def maxDistance(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

		seen = set()
		q = collections.deque()

		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					q.append(((i, j), 0))
					seen.add((i, j))
		# all waters, all lands, return -1
		if not q or len(q) == m * n:
			return -1

		res = -1 # max distance from all waters(i.e 0)
		while q:
			pos, level = q.popleft()
			level = max(level, res)
			x, y = pos[0], pos[1]
			for dd in dirs:
				x_next, y_next = x + dd[0], y + dd[1]
				if 0 <= x_next < m and 0 <= y_next < n and grid[x_next][y_next] == 0 and (x_next, y_next) not in seen:
					seen.add((x_next, y_next))
					q.append(((x_next, y_next), level + 1))

		return level