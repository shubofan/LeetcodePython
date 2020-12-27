from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]: # it has been approved that nums[i] > nums[i - 1] in previous interation
        #         return i
        # return len(nums) - 1

        l, r = 0, len(nums) - 1

        while l < r:
            mid = int(l + (r - l) / 2)

            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
