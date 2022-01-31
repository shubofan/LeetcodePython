#  Time: O(N^2)
#  Space: O(N)

# DP with LIS
from typing import List


class Solution:
	def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
		candidate = []
		n = len(ages)
		for i in range(n):
			candidate += [(ages[i], scores[i])]

		candidate.sort(key=lambda x: (x[0], x[1]))  # sort by age then score

		dp = [0] * n
		# Let dp[i] be the maximum score we can get if we choose from 0th to ith player and must pick ith player.
		# dp[i] = max( dp[j] | 0 <= j < i && scores[j] <= scores[i] ) + scores[i]
		dp[0] = candidate[0][1]

		for i in range(1, n):
			dp[i] = candidate[i][1]
			for j in range(i):
				if candidate[j][1] <= candidate[i][1]:
					dp[i] = max(dp[i], candidate[i][1] + dp[j])

		return max(dp)