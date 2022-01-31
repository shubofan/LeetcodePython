from typing import List


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		profit, low_price = 0, prices[0]

		for i in range(len(prices)):
			profit = max(profit, prices[i] - low_price)
			if prices[i] < low_price:
				low_price = prices[i]

		return profit