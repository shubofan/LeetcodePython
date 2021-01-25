class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        pre_diff = nums[1] - nums[0]

        res = 0

        # [1, 1, 1], start from 1th one, so res = 1 else starting from 0th, so res = 2
        if pre_diff == 0:
            res = 1
        else:
            res = 2

        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and pre_diff <= 0):
                res += 1
                pre_diff = diff
            if (diff < 0 and pre_diff >= 0):
                res += 1
                pre_diff = diff

        return res
