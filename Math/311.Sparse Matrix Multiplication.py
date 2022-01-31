class Solution:
	"""
	@param A: a sparse matrix
	@param B: a sparse matrix
	@return: the result of A * B
	"""
	# def multiply(self, A, B):
	#     A_m, A_n = len(A), len(A[0])
	#     B_m, B_n = len(B), len(B[0])
	#     res = [[0] * B_n for _ in range(A_m)]
	#     # print(res)
	#     for x in range(A_m):
	#         for y in range(A_n):
	#             if A[x][y]: # Calculate when this row in A has non-zero elements
	#                 for k in range(B_n):
	#                     if B[y][k]: res[x][k] += A[x][y] * B[y][k];

	#     return res

	'''
	由于是稀疏数组可以只计算非零数字。
	将A矩阵转存为hashmap,然后对每一个非零数遍历B的列数来更新它在ans矩阵里可以被用到的位置。
	'''

	def multiply(self, A, B):
		A_m, A_n = len(A), len(A[0])
		B_m, B_n = len(B), len(B[0])
		res = [[0] * B_n for _ in range(A_m)]
		v_idx = {}  # <(x, y), value>

		for x in range(A_m):
			for y in range(A_n):
				if A[x][y]:
					v_idx[(x, y)] = A[x][y]

		for pos, v in v_idx.items():
			x, y = pos[0], pos[1]
			for k in range(B_n):
				res[x][k] += v * B[y][k]  # res[x][k] = A[x][y](i.e. v) * B[y][k]
		return res