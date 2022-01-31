class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		self.res = []

		def helper(nums, start, path):
			self.res += [path]
			for i in range(start, len(nums)):
				helper(nums, i + 1, path + [nums[i]])

		helper(nums, 0, [])
		return self.res
