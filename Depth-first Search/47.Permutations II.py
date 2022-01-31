class Solution:
	def permuteUnique(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		res = []

		def dfs(nums, path, seen, res):
			if len(path) == len(nums):
				res += [path]
				return
			for i in range(len(nums)):
				# 1st, if i is used just ignore
				# 2nd, current == previous and previous not used -> To ensure there is just one current element + previous element when current element == previous element i.e.(nums[i] == nums[i - 1] and i - 1 in seen)
				if i in seen or i > 0 and nums[i] == nums[i - 1] and i - 1 in seen:
					continue
				else:
					if i not in seen:
						seen.add(i)
						dfs(nums, path + [nums[i]], seen, res)
						seen.remove(i)

		dfs(nums, [], set(), res)
		return res