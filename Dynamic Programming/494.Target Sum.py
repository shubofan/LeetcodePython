from typing import List


class Solution:
    # 0-1 backpack
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if target > s:
            return 0

        # x is number of positive elements
        # x - (sum - x) = target
        # x = target / 2
        if (s + target) % 2 == 1:
            return 0
        else:
            x = int((s + target) / 2)

        # dp[i]: number of way the fill the backpack with capacity of i
        dp = [0] * (x + 1)
        dp[0] = 1

        for num in nums:
            for i in range(x, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[-1]
