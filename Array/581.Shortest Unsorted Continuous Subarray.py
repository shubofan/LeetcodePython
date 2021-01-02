class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == sorted_nums[l]:
                l += 1
            else:
                break
        while r >= 0:
            if nums[r] == sorted_nums[r]:
                r -= 1
            else:
                break

        return 0 if r - l < 0 else r - l + 1
