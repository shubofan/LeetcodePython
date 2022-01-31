from typing import List


class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda i: (i[0], i[1]))

		l, r = intervals[0][0], intervals[0][1]
		overlaps = 0
		for i in range(1, len(intervals)):
			interval = intervals[i]
			if r >= interval[1]:  # something like (l, interval[0], interval[1], r), interval will be removed
				overlaps += 1
			elif l == interval[0] and r <= interval[
				1]:  # something like (interval[0], l, r, interval[1]), previous inteval will be removed
				overlaps += 1
				l = interval[0]
				r = interval[1]
			else:
				l = interval[0]
				r = interval[1]

		return len(intervals) - overlaps


class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda i: (i[0], -i[1])) # inteval[1] is Decreasing when sorting!

		r = 0
		not_covered = 0

		for interval in intervals:
			if interval[1] > r:
				not_covered += 1
				r = interval[1]

		return not_covered