# # Stack
# class Solution:
#     def findLengthOfLCIS(self, nums: List[int]) -> int:
#         stack = []
#         res = 0

#         for num in nums:
#             if not stack or stack[-1] < num:
#                 stack += [num]
#                 res = max(res, len(stack))
#             else:
#                 stack = [num]

#         return res


# sliding window
class Solution:
	def findLengthOfLCIS(self, nums: List[int]) -> int:
		res = 0
		l = 0

		for r in range(len(nums)):
			if r and nums[r] <= nums[r - 1]:
				l = r
			res = max(res, r - l + 1)

		return res