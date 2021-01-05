from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # count is total count of current number
        # j is the pointer used to copy the element to new array
        j, count = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            # if count <= 2, we need to use the current nums[i]
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j