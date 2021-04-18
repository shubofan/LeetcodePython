from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        res = 0
        cur = intervals[0]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= cur[1]:
                cur[1] = interval[1]
            else:
                res += 1

        return res