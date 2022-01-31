from typing import List

# Time: O(N)
# Space: O(K), key of dic is [0, k - 1], so O(K)
class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		n = len(nums)
		pre_sum = 0
		# <prefix_sum % k, last index of sub array>
		dic = {0: -1}  # such case [1,2]. k = 3

		# (a-b)%k=0 => (a%k) = (b%k)
		for i in range(n):
			pre_sum += nums[i]  # pre_sum -> a
			key = pre_sum % k

			if key in dic:  # another sub array -> b
				if i - dic[key] > 1:  # ensure sub array 's length > 1
					return True
			else:
				dic[key] = i

		return False
