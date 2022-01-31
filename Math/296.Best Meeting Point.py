class Solution:
	"""
	@param grid: a 2D grid
	@return: the minimize travel distance
	"""

	# 先考虑一维的情况，如果所有人都住在一条直线上，想要找到使总行走距离最小的一个见面点，

	# 这个见面点应当设置为所有人居住位置的中位数。

	# 推广到二维，其实就是横向找一个中位数，再纵向找一个中位数，即可得到最佳见面点，然后计算每个人到见面点的距离即可。

	# Time：O(MN  + NlogN)

	# 空间复杂度：O(MN)

	def minTotalDistance(self, grid):
		m, n = len(grid), len(grid[0])
		row = []
		col = []

		for x in range(m):
			for y in range(n):
				if grid[x][y] == 1:
					row += [x]
					col += [y]

		col.sort()

		row_median = row[len(row) // 2]
		col_median = col[len(col) // 2]

		res = 0
		for i in range(len(row)):
			res += (abs(row[i] - row_median) + abs(col[i] - col_median))

		return res
