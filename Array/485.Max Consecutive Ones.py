from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        consecutiveOnes = 0

        for i in nums:
            if i == 1:
                consecutiveOnes += 1
            else:
                res = max(res, consecutiveOnes)
                consecutiveOnes = 0

        return max(res, consecutiveOnes)
