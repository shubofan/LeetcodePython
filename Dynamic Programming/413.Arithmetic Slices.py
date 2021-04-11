class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        res = 0
        dp = 0
        # dp: 以i结尾的等差数列的个数
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp += 1
                res += dp
            else:
                dp = 0

        return res