class Solution:
	# Time O(NlogN)
	# Space O(1) for python
	def numSubseq(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)
		res = 0
		mod = 10 ** 9 + 7
		l, r = 0, n - 1
		while l <= r:
			'''
			for each elements in the subarray A[l+1] ~ A[r],
			we can pick or not pick,
			so there are 2 ^ (r - l) subsequences in total.
			'''
			if nums[l] + nums[r] <= target:
				res += pow(2, r - l) % mod
				l += 1
			else:
				r -= 1

		return res % mod
