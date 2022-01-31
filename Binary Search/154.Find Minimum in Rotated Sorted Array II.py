from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l, r = 0, n - 1
        # if nums[m] > nums[r], min should be always in [m + 1, r] (explained in Essence). To satisfy the invariant, l = m + 1;
        # if nums[m] < nums[l], min should be always in [l + 1, m] (explained in Essence), to satisfy the assertion, hi = mi, lo = lo + 1;
        # else (nums[l] <= nums[m] <= nums[r]), min should be always nums[l].
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: #  if nums[m] > nums[r], min should be always in [m + 1, r] (explained in Essence). To satisfy the invariant, l = m + 1;
                l = m + 1
            elif nums[m] < nums[r]: # if nums[m] < nums[r], min should be always in [l, m] (explained in Essence)
                r = m
            else: # When num[m] == num[r], we couldn't sure the position of minimum in mid's left or right, so just let upper bound reduce one.
                r -= 1
        return nums[l]
