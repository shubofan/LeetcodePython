from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals:
            return [newInterval]

        i, n = 0, len(intervals)

        # current interval is before newInterval, no overlap
        while i < n and intervals[i][1] < newInterval[0]:
            res += [intervals[i]]
            i += 1
        # there is an overlap, so need to update newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res += [newInterval]

        # current interval is after newInterval, no overlap
        while i < n:
            res += [intervals[i]]
            i += 1
        return res