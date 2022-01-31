class ProductOfNumbers:

	def __init__(self):
		self.prefix_product = [1]

	def add(self, num: int) -> None:
		if num == 0:
			self.prefix_product = [1]
		else:
			last = self.prefix_product[-1]
			self.prefix_product += [num * last]

	def getProduct(self, k: int) -> int:
		i = len(self.prefix_product) - 1
		if i - k < 0:
			return 0
		return self.prefix_product[i] // self.prefix_product[i - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)