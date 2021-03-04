from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        # If the current value is in the range of [1,length] and it's not at its correct position, for example 3 should be placed at index 2
        # swap it to its correct position.
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
