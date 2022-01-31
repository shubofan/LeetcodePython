from typing import List


class Solution:
	#
	# Time O(n × log( sum(n) − max(n) ))  log(sum(n)−max(n)) times binary search, each binary search take O(n)
    # space O(1)
	def splitArray(self, nums: List[int], m: int) -> int:
		# check total number splits and so for each split, sum of split < target_sum
		def checkSum(nums, m, target_sum):
			cur_sum = 0
			splits = 1 # number of split
			for num in nums:
				if cur_sum + num > target_sum:  # need to add a split
					splits += 1
					cur_sum = num
				else:
					cur_sum += num
			return splits <= m

		# 使用「二分查找」确定一个恰当的「子数组各自的和的最大值」，
		# 使得它对应的「子数组的分割数」恰好等于 m
		l, r = max(nums), sum(nums)
		while l < r:
			mid = (l + r) // 2
			if checkSum(nums, m, mid):  # if mid is 子数组各自的和的最大值, splits <= m, so r is possible, and try to find a smaller 子数组各自的和的最大值.
				r = mid  # If splits == m, continue shrink, since mid may not in the array, so we need to lower it until it == left. for example [1, 100], m = 2, first mid == 50,  checkSum([1, 100], 2, 50) == True, but we need to continue lower it, continue mid == left = 1
			else:
				l = mid + 1  # mid is not possible, so l = mid + 1 -> 子数组各自的和的最大值 need to be bigger 去减小 splits 的数目

		return l