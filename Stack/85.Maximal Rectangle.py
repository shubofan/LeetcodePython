class Solution:
	# time: O(MN), for stack operation, each element in matrix at most each push into/pop from stack 1 time, so still O(MN) overall
	# space; O(n), the array of height
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		if not matrix:
			return 0
		m, n = len(matrix), len(matrix[0])

		# height 初始化的大小为 n+1，为什么要多一个呢？
		# 这是因为我们只有在当前位置小于等于前一个位置的高度的时候，才会去计算矩形的面积，假如最后一个位置的高度是最高的，那么我们就没法去计算并更新结果 res 了，所以要在最后再加一个高度0，这样就一定可以计算前面的矩形面积了
		height = [0] * (n + 1)  # height[i] -> for each row, the height of index i
		res = 0

		for row in matrix:
			for col in range(n):
				height[col] = height[col] + 1 if row[col] == '1' else 0

			stack = [-1]
			for col in range(n + 1):
				# monotone increase stack
				while height[col] < height[stack[-1]]:
					h = height[stack.pop()]
					w = col - stack[-1] - 1

					res = max(res, h * w)
				stack += [col]
		return res