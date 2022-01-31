'''
Time complexity : O(n). The entire nums array is traversed only once.

Space complexity : O(n) Hashmap map can contain upto n distinct entries in the worst case.
'''
import collections
from typing import List


class Solution:
	def subarraysDivByK(self, nums: List[int], k: int) -> int:
		dic = collections.defaultdict(int)
		cur_sum = 0
		res = 0

		# for two sub array A and B, if sum(A) % k == sum(B) % k , then (A-B) % k == 0
		for num in nums:
			cur_sum_mod = (cur_sum + num) % k

			# 1st: cur_sum_mod -> cur_sum can be divided by k
			if cur_sum_mod == 0:
				res += 1

			# 2nd, cur_sum, and previous sum of sub array has same reminder
			res += dic[cur_sum_mod]

			dic[cur_sum_mod] += 1

		return res