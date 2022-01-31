from typing import List


class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		if not intervals:
			return 0
		intervals.sort(key=lambda x: (x[1], x[0]))  # sort based on end
		end = intervals[0][1]
		res = 0
		for i in range(1, len(intervals)):
			interval = intervals[i]

			if interval[0] < end:  # to_be_removed
				res += 1
			else:
				end = interval[1]
		return res
