class Solution:
	def fib(self, n: int) -> int:
		self.cache = [-1] * 31
		self.cache[0] = 0
		self.cache[1] = 1
		return self.mem(n)

	def mem(self, n: int) -> int:
		if self.cache[n] >= 0:
			return self.cache[n]
		self.cache[n] = self.mem(n - 1) + self.mem(n - 2)
		return self.cache[n]