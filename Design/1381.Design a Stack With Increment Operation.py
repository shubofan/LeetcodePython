# Regular solution, increment take O(k)
# class CustomStack:

#     def __init__(self, maxSize: int):
#         self.s = []
#         self.maxSize = maxSize

#     def push(self, x: int) -> None:
#         if len(self.s) == self.maxSize:
#             return
#         self.s += [x]


#     def pop(self) -> int:
#         if len(self.s) == 0:
#             return -1
#         return self.s.pop()

#     def increment(self, k: int, val: int) -> None:

#         if k >= len(self.s):
#             # map(lambda x+val: self.s)
#             # print(self.s)
#             self.s = list(map(lambda x: x + val, self.s))
#             # print(self.s)
#         else:
#             for i in range(k):
#                 self.s[i] += val

# Lazy increment, to make increment O(1)
class CustomStack:

	def __init__(self, maxSize: int):
		self.s = []
		self.incr = []
		self.maxSize = maxSize

	def push(self, x: int) -> None:
		if len(self.s) == self.maxSize:
			return
		self.s += [x]
		self.incr += [0]

	def pop(self) -> int:
		if len(self.s) == 0:
			return -1
		return self.s.pop() + self.incr.pop()

	def increment(self, k: int, val: int) -> None:
		for i in range(min(k, len(self.incr))):
			self.incr[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)