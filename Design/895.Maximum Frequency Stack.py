from collections import Counter, defaultdict


# It is guaranteed that there will be at least one element in the stack before calling pop. (Ask this at first, if not guaranteed, need add check in pop() function)

from collections import Counter, defaultdict


class FreqStack:

	def __init__(self):
		self.fre = Counter()  # <value, frequency>
		self.most_freq = 0
		self.group = defaultdict(list)  # <frequency, [] of values with same frequency>

	def push(self, val: int) -> None:
		self.fre[val] += 1

		self.group[self.fre[val]].append(val)
		self.most_freq = max(self.most_freq, self.fre[val])

	def pop(self) -> int:
		x = self.group[self.most_freq].pop()
		self.fre[x] -= 1

		if not self.group[self.most_freq]:
			self.most_freq -= 1
		return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()