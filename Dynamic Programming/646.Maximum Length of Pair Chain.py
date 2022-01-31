# sort + LIS(longest increase sequence)
from typing import List


class Solution:
	def findLongestChain(self, pairs: List[List[int]]) -> int:
		pairs.sort(key=lambda x: (x[0], x[1]))

		n = len(pairs)

		dp = [1] * n

		for i in range(n):
			for j in range(i):
				pre = pairs[j]
				cur = pairs[i]
				if cur[0] > pre[1]:
					dp[i] = max(dp[i], dp[j] + 1)

		return max(dp)