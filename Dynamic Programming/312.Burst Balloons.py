# Time complexity : O(N^3). There are N^2(left, right) pairs and it takes O(N) to find the value of one of them.

# Space complexity : O(N^2). This is the size of dp .

class Solution:
	def maxCoins(self, nums: List[int]) -> int:

		# add 1 at head and tail to handle edge case
		nums.insert(0, 1)
		nums += [1]

		n = len(nums)

		# dp[i][j] means the max coin is in open range(i, j)
		dp = [[0] * n for _ in range(n)]

		# get max in open range(l, r) -> max coins if we burst balloons [l+1, r-1]
		def getMaxInRange(nums, l, r):
			res = 0
			# i is the last Balloon we want to burst, i in [l+1, r-1]
			for i in range(l + 1, r):
				res = max(res, dp[l][i] + nums[l] * nums[i] * nums[r] + dp[i][r])

			return res

		# length of the open range, start from 2
		for length in range(2, n):
			for i in range(n - length):  # start from 0, for each length, get the max in open range(i, i+length)
				dp[i][i + length] = getMaxInRange(nums, i, i + length)

		return dp[0][-1]  # maxCoins in the open range(0, len(nums)) -> maxCoins in the close range[1, len(nums) - 1] which is the original balloons list
