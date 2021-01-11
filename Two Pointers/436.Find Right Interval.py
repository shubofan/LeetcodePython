class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        if not intervals:
            return res
        n = len(intervals)
        res = [-1] * n
        dic = {}
        # We need to keep original interval with its index in the list
        for idx, interval in enumerate(intervals):
            dic[interval[0]] = idx

        intervals = sorted(intervals, key=lambda x: x[0])

        for i, interval in enumerate(intervals):
            if i == n - 1:
                continue
            l, r = i + 1, n - 1
            while l < r:
                mid = int(l + (r - l) / 2)
                if intervals[mid][0] >= interval[1]:
                    r = mid
                else:
                    l = mid + 1
            # If intervals[l][0]  >= interval[1], found the right interval(i.e. intervals[l]) else it should be -1
            if intervals[l][0] >= interval[1]:
                # get original index of the interval
                res[dic[intervals[i][0]]] = dic[intervals[l][0]]

        return res
