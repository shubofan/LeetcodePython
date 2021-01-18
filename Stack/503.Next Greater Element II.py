class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        res = [-1] * n

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack += [i]

        # For the remaining elements in the stack, find next greater again from begin
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            if not stack:
                break
        return res
