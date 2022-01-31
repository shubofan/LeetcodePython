import collections
from typing import List

'''
Time complexity : O(n). The entire nums array is traversed only once.

Space complexity : O(n) Hashmap map can contain upto n distinct entries in the worst case. 
'''

#
class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		prefix_sum = collections.defaultdict(int)
		res = 0
		cur_sum = 0
		for num in nums:
			cur_sum += num
			# situation 1:
			# continuous subarray starts
			# from the beginning of the array
			if cur_sum == k:
				res += 1

			# situation 2:
			# number of times the cur_sum − k has occurred already, -> sum of continuous subarray is cur_sum - (cur_sum − k ) = k
			# determines the number of times a subarray with sum k
			# has occurred up to the current index
			res += prefix_sum[cur_sum - k]
			prefix_sum[cur_sum] += 1
		return res
