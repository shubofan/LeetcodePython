class Solution:
	# Greedy to get the rightmost two point
	def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
		if not intervals:
			return 0

		intervals.sort(key=lambda x: (x[1], -x[0]))

		left, right = intervals[0][1] - 1, intervals[0][1]
		res = 2

		for i in range(1, len(intervals)):
			interval = intervals[i]

			# 1. one element of the set is in the interval
			if left < interval[0] <= right:
				res += 1
				left = right
				right = interval[1]

			# 2. no element of the set is in the interval
			elif interval[0] > right:
				res += 2
				left = interval[1] - 1

				right = interval[1]

		return res