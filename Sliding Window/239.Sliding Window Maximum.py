import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        # index is increase, val is decreasing
        for i in range(k):
            # ensure q is monotone decreasing , so nums[q[0]] is always largest
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        res = []
        res += [nums[q[0]]]

        for i in range(k, n):
            # pop from left for those elements no longer in the window
            while q and q[0] + k <= i:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            res += [nums[q[0]]]
        return res

