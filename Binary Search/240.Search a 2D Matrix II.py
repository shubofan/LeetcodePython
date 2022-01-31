from typing import List


class Solution:
	# O(lg(n)+lg(n−1)+lg(n−2)+…+lg(1))=O(lg(n⋅(n−1)⋅(n−2)⋅…⋅1))=O(lg(n!))

	# Space complexity : O(1)
	# search diagonals
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		m, n = len(matrix), len(matrix[0])
		diagonals = min(m, n)

		for i in range(diagonals):
			row = matrix[i][i:]
			col = [row[i] for row in matrix]
			if self.search(row, target) or self.search(col, target):
				return True

		return False

	def search(self, row: List[int], target: int) -> bool:
		l, r = 0, len(row) - 1
		while l < r:
			mid = (l + r) // 2
			if row[mid] < target:
				l = mid + 1
			else:
				r = mid
		return row[l] == target


