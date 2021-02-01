from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product, r_product = [1] * len(nums), 1
        res = [1] * len(nums)

        # l_product product before i, not including nums[i]
        # no left element before 0, so l_product[0] = 1
        for i in range(1, len(nums)):
            l_product[i] = l_product[i - 1] * nums[i - 1]

        # r_product product after j, not including nums[j]
        # no right element after 0, so r_product[-1] = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = r_product * l_product[j]
            r_product *= nums[j]

        return res