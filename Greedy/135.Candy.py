from typing import List


class Solution:
	def candy(self, ratings: List[int]) -> int:
		# Two rules

		n = len(ratings)
		res = [1] * n

		# 1st rule: From left to right, and A is in the left of B, if ratings[B] > ratings[A], assigned candy + 1
		for i in range(1, n):
			if ratings[i] > ratings[i - 1]:
				res[i] = res[i - 1] + 1

		# 2nd rule: From right to left, and B is in the right of A, if ratings[B] > ratings[A], assigned candy + 1
		for i in range(n - 2, -1, -1):
			if ratings[i] > ratings[i + 1]:
				res[i] = max(res[i], res[i + 1] + 1)  # use max to ensure 1st rule and 2nd rule can be meet together
		return sum(res)