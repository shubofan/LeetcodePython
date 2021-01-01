class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0

        # pick up all non-zero elements
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                fast += 1
                slow += 1
            else:
                fast += 1
        # fill remaining elements with 0s
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
