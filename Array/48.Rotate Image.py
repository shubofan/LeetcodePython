class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		m = len(matrix)

		# flip against diagonal
		for i in range(m):
			for j in range(i, m):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		# flip the matrix vertically
		for i in range(m):
			for j in range(m // 2):
				matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j], matrix[i][j]