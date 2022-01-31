from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		res = []
		r0, c0 = 0, 0
		r1, c1 = len(matrix) - 1, len(matrix[0]) - 1

		while r0 <= r1 and c0 <= c1:

			for i in range(c0, c1 + 1):
				res += [matrix[r0][i]]

			for i in range(r0 + 1, r1 + 1):
				res += [matrix[i][c1]]

			if r0 < r1 and c0 < c1:
				for i in range(c1 - 1, c0, -1):
					res += [matrix[r1][i]]

				for i in range(r1, r0, -1):
					res += [matrix[i][c0]]

			r0 += 1
			r1 -= 1
			c0 += 1
			c1 -= 1

		return res