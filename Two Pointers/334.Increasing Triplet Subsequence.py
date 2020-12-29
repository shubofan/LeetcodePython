from math import inf
from typing import List


class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     if len(nums) < 3:
    #         return False
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             if nums[j] > nums[i]:
    #                 for k in range(j, len(nums)):
    #                     if nums[k] > nums[j]:
    #                         return True
    #     return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        small = mid = float(inf)
        for num in nums:
            if num <= small:
                small = num
            elif num <= mid:
                mid = num
            else:
                return True
        return False
