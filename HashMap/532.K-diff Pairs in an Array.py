import collections
from typing import List


class Solution:
	def findPairs(self, nums: List[int], k: int) -> int:
		res = 0
		cnt = collections.Counter(nums)

		for num, fre in cnt.items():
			# Since k> 0 , we just need find pair like (1, 4), we won't find (4,1)
			if k > 0 and num + k in cnt:
				res += 1
			# For example, if we have nums = [1,1,1,1] and k = 0 , we have one unique (1,1) pair number of 1 must > 1
			if k == 0 and cnt[num] > 1:
				res += 1
		return res