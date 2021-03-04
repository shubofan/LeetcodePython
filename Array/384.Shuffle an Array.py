import random as r
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        a = self.nums[::]
        # 分析洗牌算法正确性的准则：产生的结果必须有 n! 种可能
        for i in range(len(a)):
            idx = r.randint(0, len(a) - 1)  # random int [0, len(a) - 1]
            a[i], a[idx] = a[idx], a[i]
        return a

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()