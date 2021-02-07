from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse entire array at first
        nums.reverse()

        k %= len(nums)

        # reverse [0:k)
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1

        l = k
        r = len(nums) - 1

        # reverse [k:n)
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1
