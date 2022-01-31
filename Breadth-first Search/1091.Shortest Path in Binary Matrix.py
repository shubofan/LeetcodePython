import collections

# Time: O (MN), search the entire grid
# Space: O (1), queue
class Solution:
	def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])

		target = (m - 1, n - 1)

		q = collections.deque()
		if grid[0][0] == 1:
			return -1

		q += [((0, 0), 1)]
		# set value to 1 to mark the position as visited
		grid[0][0] = 1

		dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

		while q:
			pos, level = q.popleft()

			if pos == target:
				return level

			x, y = pos[0], pos[1]

			for d in dirs:
				nx, ny = x + d[0], y + d[1]

				if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
					grid[nx][ny] = 1
					q += [((nx, ny), level + 1)]
		return -1