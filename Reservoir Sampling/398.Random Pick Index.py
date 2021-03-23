import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 1
        pick = None
        for idx, num in enumerate(self.nums):
            if num == target:
                prob = random.randint(1, count)
                if prob == count:
                    pick = idx
                count += 1
        return pick

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)