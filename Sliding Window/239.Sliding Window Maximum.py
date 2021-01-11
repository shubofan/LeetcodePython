import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        res = []
        n = len(nums)
        q = collections.deque()

        # keep index of nums in deque is decreasing However value of nums is increasing
        for i in range(k):
            if not q:
                q.append(i)
            else:
                while q and nums[q[0]] <= nums[i]:
                    q.popleft()
                q.appendleft(i)

        res += [nums[q[-1]]]

        for i in range(k, n):
            # pop the right most element in deque since the index of nums in q[-1] in smallest
            if q and q[-1] + k <= i:
                q.pop()

            # to keep the deque which value of nums is increasing
            while q and nums[q[0]] <= nums[i]:
                q.popleft()
            q.appendleft(i)
            res += [nums[q[-1]]]

        return res