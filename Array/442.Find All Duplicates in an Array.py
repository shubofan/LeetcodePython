from typing import List

# O(n) with no extra space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # for a given element i, if nums[i] < 0, it means i appeared before.
        for i in nums:
            # find the correct index to be change
            index = abs(i) - 1
            # i appeared before
            if nums[index] < 0:
                res += [abs(i)]
            else:
                # mark corresponding element to negative
                nums[index] *= -1
        return res
