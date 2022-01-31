# Time: O(n)
# Space: O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        l, r = 0, 0
        product = 1
        while r < n:
            product *= nums[r]
            while l < r and product >= k:
                product //= nums[l]
                l += 1
            if product < k: # nums = [1,2,3], k = 0
                res += (r - l + 1)
            r += 1
        return res