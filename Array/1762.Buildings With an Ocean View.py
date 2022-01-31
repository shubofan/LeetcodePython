from typing import List


class Solution:
	def findBuildings(self, heights: List[int]) -> int:
		max_h = 0
		n = len(heights)
		res = []
		for i in range(n-1,-1,-1):
			if heights[i] > max_h:
				res += [i]
				max_h = heights[i]

		return res[::-1]


class Solution:
	def findBuildings(self, heights: List[int]) -> int:
		stack = []

		n = len(heights)
		for i in range(n):
			while stack and heights[stack[-1]] <= heights[i]:
				stack.pop()
			stack += [i]


		return stack