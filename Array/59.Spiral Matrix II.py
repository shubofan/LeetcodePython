from typing import List


class Solution:
	def generateMatrix(self, n: int) -> List[List[int]]:
		res = [[0] * n for _ in range(n)]
		r0, r1, c0, c1 = 0, n - 1, 0, n - 1
		num = 1
		while r0 <= r1 and c0 <= c1:
			for i in range(c0, c1 + 1):
				res[r0][i] = num
				num += 1
			r0 += 1

			for i in range(r0, r1 + 1):
				res[i][c1] = num
				num += 1
			c1 -= 1

			for i in range(c1, c0, -1):
				res[r1][i] = num
				num += 1
			r1 -= 1

			for i in range(r1 + 1, r0 - 1, -1):
				res[i][c0] = num
				num += 1
			c0 += 1

		return res
