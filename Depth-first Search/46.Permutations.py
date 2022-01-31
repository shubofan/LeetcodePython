class Solution:
	# time O(N!) factorial n
	def permute(self, nums: List[int]) -> List[List[int]]:
		self.res = []

		self.helper(nums, [], set())
		return self.res

	def helper(self, nums: List[int], path: List[int], seen: set) -> None:

		if len(path) == len(nums):
			self.res += [path]
			return
		for i in range(len(nums)):
			if nums[i] not in seen:
				seen.add(nums[i])
				self.helper(nums, path + [nums[i]], seen)
				seen.remove(nums[i])