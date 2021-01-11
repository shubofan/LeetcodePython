from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if n == 1:
            return 0 if nums[0] == target else -1

        #  find min element
        l, r = 0, n - 1
        while l < r:
            m = int(l + (r - l) / 2)

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        if nums[l] == target:
            return l

        min_idx = l
        l, r = 0, n - 1

        # right is ordered
        if nums[min_idx] < target <= nums[-1]:
            l = min_idx
        else:
            r = min_idx

        # search from ordered range
        while l < r:
            m = int(l + (r - l) / 2)
            if nums[m] == target:
                return m

            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1 if nums[l] != target else l
