from typing import List


class Solution:
	# fewest number of coins that you need to make up that amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]