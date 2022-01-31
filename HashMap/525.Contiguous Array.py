# Time complexity : O(n) The entire array is traversed only once.

# Space complexity : O(n)
from typing import List


class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		n = len(nums)
		# convert arr to array just contains 1, or -1
		for i in range(n):
			if nums[i] == 0:
				nums[i] = -1

		# map <sum of sub array, end index of sub array>
		dic = {}
		res = 0
		cur_sum = 0

		# if dic[A] == dic[B] -> sum of [A:B] must be 0 -> number of -1 == number of 1 -> number of 0 == number of 1
		for i, num in enumerate(nums):
			cur_sum += num
			# sum of sub array [0:i] == 0
			if cur_sum == 0:
				res = max(i + 1, res)

			# if sum of sub array [0:i] == sum of sub array [0:dic[cur_sum]], sum(array [dic[cur_sum]+1:i]) == 0
			# array [dic[cur_sum]+1:i] is a valid sub array-> length of it is i- (dic[cur_sum]+1) + 1 =  i- dic[cur_sum]

			if cur_sum in dic: # sum(array [dic[cur_sum]+1:i]) == 0
				res = max(res, i - dic[cur_sum])
			else:
				dic[cur_sum] = i
		return res