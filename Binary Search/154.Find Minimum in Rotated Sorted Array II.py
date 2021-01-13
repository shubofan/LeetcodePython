from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        res = float('inf')
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == nums[l]:
                l += 1
                res = min(res, nums[m])
            # right is ordered, update res with smallest in right, then search left
            elif nums[m] < nums[l]:
                res = min(res, nums[m])
                r = m - 1
            # left is ordered, update res with smallest in left, then search right
            else:
                res = min(res, nums[l])
                l = m + 1
        return res
