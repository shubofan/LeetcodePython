from typing import List

# O(n) Time with no extra space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        # for a given element i, if nums[i] < 0, it means i appeared before.
        for num in nums:
            # find the correct index to be change, so it appear twice in the array
            index = abs(num) - 1
            # i appeared before
            if nums[index] < 0:
                res += [abs(num)]
            else:
                # mark corresponding element to negative
                nums[index] *= -1
        return res
