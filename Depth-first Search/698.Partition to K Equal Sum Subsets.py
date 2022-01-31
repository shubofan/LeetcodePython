class Solution:
	# Time(2^n), total 2^n subsets will be generated
	def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

		def dfs(nums, start, seen, cur_sum, k, target):
			if k == 1:
				return True

			# help Prune
			if cur_sum > target:
				return

			# get the a valid subset, then find another one
			if target == cur_sum:
				return dfs(nums, 0, seen, 0, k - 1, target)

			for i in range(start, len(nums)):
				if i not in seen:
					seen.add(i)
					if dfs(nums, i + 1, seen, cur_sum + nums[i], k, target):
						return True
					seen.remove(i)

			return False

		n = len(nums)

		if sum(nums) % k != 0:
			return False
		target = sum(nums) // k
		# help Prune
		nums.sort(reverse=True)

		return dfs(nums, 0, set(), 0, k, target)
