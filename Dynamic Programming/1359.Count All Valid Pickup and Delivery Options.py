class Solution:
	def countOrders(self, n: int) -> int:
		# The first place must be a delivery, and we can pick from D1 to DN so total n options
		# The for the corresponding P, we have 2 * N - 1 positions to place

		# So there would be n * (2 * n - 1) options for 1st (D, P) order
		# Then there would be (n - 1) * (2 * (n-1) - 1) for the 2nd (D, P) order

		# Then there would be 2 * (2 * (2-1) - 1) for the n - 1(th) (D, P) order

		# Then there would be 1 for the n(th) (D, P) order

		# In total, n! * (1 * 3 * 5 * ...* 2 * (n - 1)) Options

		res = 1
		for i in range(2, n + 1):
			res *= i * (2 * i - 1)
		return res % (10 ** 9 + 7)