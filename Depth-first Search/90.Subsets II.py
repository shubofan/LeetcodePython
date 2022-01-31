from typing import List

# res as a global variable
class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		self.res = []
		nums.sort()

		def dfs(subset, start):
			self.res += [subset]
			if start == len(nums):
				return

			for i in range(start, len(nums)):
				if i != start and nums[i] == nums[
					i - 1]:  # for each deplicte number, we just add it when it enter the loop first time
					continue
				dfs(subset + [nums[i]], i + 1)

		dfs([], 0)
		return self.res

class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		self.res = []
		nums.sort()

		def dfs(subset, start):
			self.res += [subset]
			if start == len(nums):
				return

			for i in range(start, len(nums)):
				if i != start and nums[i] == nums[
					i - 1]:  # for each deplicte number, we just add it when it enter the loop first time
					continue
				dfs(subset + [nums[i]], i + 1)

		dfs([], 0)
		return self.res
class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort()

		def dfs(subset, start, res):
			res += [subset]
			if start == len(nums):
				return

			for i in range(start, len(nums)):
				if i != start and nums[i] == nums[
					i - 1]:  # for each duplicate number, we just add it when it enter the loop first time
					continue
				dfs(subset + [nums[i]], i + 1, res)

		dfs([], 0, res)
		return res


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup(['1', '2']))