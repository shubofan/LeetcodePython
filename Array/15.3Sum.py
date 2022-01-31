from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        if n <= 2:
            return []
        # total O(N^2)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            # So if l move to right x and right will move left x
            # so the l and r will move N in total, hence the time complexity is O(N)
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res += [[nums[i], nums[l], nums[r]]]
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res