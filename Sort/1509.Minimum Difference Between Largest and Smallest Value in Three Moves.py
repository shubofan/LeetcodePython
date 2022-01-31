# If we can do 0 move, return max(A) - min(A)
# If we can do 1 move, return min(the 2nd_max(A) - min(A), the max(A) - 2nd_min(A))
class Solution:
	def minDifference(self, nums: List[int]) -> int:
		if len(nums) <= 3:
			return 0
		nums.sort()

		return min(nums[-1] - nums[3], nums[-2] - nums[2], nums[-3] - nums[1], nums[-4] - nums[0])

