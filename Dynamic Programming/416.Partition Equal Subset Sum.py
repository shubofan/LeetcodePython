class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for i in range(len(nums))]

        # dp[i][j], choose any element from[0, i], if the sum of element == j
        for i in range(len(dp)):
            dp[i][0] = True

        # max element > target, return False
        if max(nums) > target:
            return False

        dp[0][nums[0]] = True

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # if j > nums[i], nums[i] can be select or not
                if j > nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                    # otherwise dp[i] cannot be selected
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(nums) - 1][target]
