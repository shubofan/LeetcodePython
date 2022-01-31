from typing import List


class Solution:
	def regionsBySlashes(self, grid: List[str]) -> int:
		n = len(grid)
		# matrix = [[True] * (n * 3) for _ in range(n*3)]

		matrix = [[True for j in range(n * 3)] for i in range(n * 3)]

		for i in range(n):
			for j in range(n):
				if grid[i][j] == '/':
					matrix[i * 3][j * 3 + 2] = False
					matrix[i * 3 + 1][j * 3 + 1] = False
					matrix[i * 3 + 2][j * 3] = False
				elif grid[i][j] == '\\':
					matrix[i * 3][j * 3] = False
					matrix[i * 3 + 1][j * 3 + 1] = False
					matrix[i * 3 + 2][j * 3 + 2] = False

		seen = set()
		count = 0

		for i in range(3 * n):
			for j in range(3 * n):
				if matrix[i][j] and (i, j) not in seen:
					count += 1
					stack = [(i, j)]
					while stack:
						x, y = stack.pop()
						seen.add((x, y))
						if x - 1 >= 0 and matrix[x - 1][y] and (x - 1, y) not in seen:
							stack += [(x - 1, y)]

						if x + 1 < 3 * n and matrix[x + 1][y] and (x + 1, y) not in seen:
							stack += [(x + 1, y)]

						if y - 1 >= 0 and matrix[x][y - 1] and (x, y - 1) not in seen:
							stack += [(x, y - 1)]

						if y + 1 < 3 * n and matrix[x][y + 1] and (x, y + 1) not in seen:
							stack += [(x, y + 1)]
		return count