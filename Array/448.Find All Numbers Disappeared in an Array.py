from typing import List

# Time Complexity : O(N)
# Space Complexity : O(1) since we are reusing the input array itself as a hash table
# and the space occupied by the output array doesn't count toward the space complexity of the algorithm.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # For each element nums[i], mark the element at the corresponding location negative if it's not already marked
        for i in range(n):

            # nums[i] should be placed to idx
            idx = abs(nums[i]) - 1

            if 0 <= idx < n and nums[idx] > 0:
                nums[idx] *= -1  # nums[i] appeared before

        res = []

        for i in range(n):
            if nums[i] > 0:  # i + 1 does not appear
                res += [i + 1]
        return res