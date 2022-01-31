from collections import defaultdict


class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		d = defaultdict(list)
		m, n = len(mat), len(mat[0])

		for i in range(m):
			for j in range(n):
				d[i + j] += [(i, j)]

		for k, v in d.items():
			if k % 2 == 0:
				v.reverse()

		res = []
		for k in sorted(d.keys()):
			for point in d[k]:
				res += [mat[point[0]][point[1]]]
		return res