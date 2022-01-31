class Solution:
	# Time complexity : O(n). n numbers are pushed and popped.

	# Space complexity : O(n) Stack is used.
	def largestRectangleArea(self, heights: List[int]) -> int:
		stack = [(-1, 0)]
		res = 0
		n = len(heights)
		# a monotone increasing stack
		for i, h in enumerate(heights):
			while stack and h <= stack[-1][1]:
				cur_h = stack.pop()[1]
				if stack:
					cur_width = i - stack[-1][0] - 1
				else:
					cur_width = i
				res = max(res, cur_h * cur_width)

			stack += [(i, h)]
		print(stack, res)
		while stack:
			cur_h = stack.pop()[1]
			if stack:
				cur_width = n - stack[-1][0] - 1
			else:
				cur_width = n
			res = max(res, cur_h * cur_width)

		return res


class Solution:
	# Time complexity : O(n). n numbers are pushed and popped.

	# Space complexity : O(n) Stack is used.
	def largestRectangleArea(self, heights: List[int]) -> int:
		stack = [(-1, 0)]
		res = 0
		n = len(heights)

		# a monotone increasing stack
		for i, h in enumerate(heights):
			# make sure don't pop (-1, 0), so len(stack) always > 1
			while len(stack) > 1 and h <= stack[-1][1]:
				cur_h = stack.pop()[1]
				cur_width = i - stack[-1][0] - 1
				res = max(res, cur_h * cur_width)

			stack += [(i, h)]

		# print(stack, res)
		while len(stack) > 1:
			cur_h = stack.pop()[1]
			cur_width = n - stack[-1][0] - 1
			res = max(res, cur_h * cur_width)

		return res