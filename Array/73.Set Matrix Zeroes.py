from typing import List

# class Solution:
#     # Time O(MN)
#     # Space O(M + N)
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         col = set()
#         row = set()

#         m, n = len(matrix), len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row.add(i)
#                     col.add(j)


#         for i in range(m):
#             for j in range(n):
#                 if i in row or j in col:
#                     matrix[i][j] = 0



class Solution:
	# Time O(MN)
	# Space O(1)
	def setZeroes(self, matrix: List[List[int]]) -> None:
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		first_col = False  # if 1st column need to be set to all 0
		first_row = False  # if 1st row need to be set to all 0

		m, n = len(matrix), len(matrix[0])

		for i in range(n):
			if matrix[0][i] == 0:
				first_row = True
		for i in range(m):
			if matrix[i][0] == 0:
				first_col = True

			# If an element is zero, we set the first element of the corresponding row and column to 0
		for i in range(1, m):
			for j in range(1, n):
				if matrix[i][j] == 0:
					matrix[i][0] = 0
					matrix[0][j] = 0

		# Iterate over the array once again and using the first row and first column, update the elements.
		for i in range(1, m):
			for j in range(1, n):
				if matrix[i][0] == 0 or matrix[0][j] == 0:
					matrix[i][j] = 0

		# update 1st row
		if first_row:
			for i in range(n):
				matrix[0][i] = 0

		# update 1st column
		if first_col:
			for i in range(m):
				matrix[i][0] = 0