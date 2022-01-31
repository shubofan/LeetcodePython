from typing import List


class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		# dp[i] means ways to compose amount i

		dp = [0] * (amount + 1)
		dp[0] = 1
		# For each coin, loop over all amounts from 0 to amount :
		# For each amount x, compute the number of combinations: dp[x] += dp[x - coin] .
		for coin in coins:
			for i in range(coin, len(dp)):
				dp[i] += (dp[i - coin])

		return dp[-1]
