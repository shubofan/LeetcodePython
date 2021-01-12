from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = set()
        if n < 4:
            return res
        nums = sorted(nums)

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    s = nums[i] + nums[j] + nums[k]
                    if s + nums[k + 1] > target or s + nums[-1] < target:
                        continue
                    else:
                        l, r = k + 1, n - 1
                        while l < r:
                            mid = (l + r) // 2
                            if nums[mid] + s < target:
                                l = mid + 1
                            else:
                                r = mid
                        if s + nums[l] == target:
                            res.add((nums[i], nums[j], nums[k], nums[l]))
        return res
    