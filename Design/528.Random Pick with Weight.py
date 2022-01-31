import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.pre_sum = []
        for weight in w:
            if not self.pre_sum:
                self.pre_sum += [weight]
            else:
                self.pre_sum += [weight + self.pre_sum[-1]]

    def pickIndex(self) -> int:

        target = random.randint(1, self.pre_sum[-1])
        # for idx, s in enumerate(self.pre_sum):
        #     if target <= s:
        #         return idx

        l, r = 0, len(self.pre_sum) - 1
        while l < r:
            mid = (l + r) // 2
            if self.pre_sum[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
