from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = []
        # for each num if nums, increment it by n, so that nums[num - 1] always > n
        for num in nums:
            nums[(num - 1) % n] += n

        # then go through the list again, if certain element is < n, it is a missing one since it was not incremented
        # previously
        res = [idx + 1 for idx, num in enumerate(nums) if num <= n]
        return res