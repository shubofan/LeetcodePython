class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        pre = nums[0]
        moves = 0
        for i in range(1, n):
            if nums[i] <= pre:
                moves += pre + 1 -nums[i]
                nums[i] = pre + 1
            pre = nums[i]
        return moves