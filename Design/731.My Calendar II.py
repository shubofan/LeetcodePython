class MyCalendarTwo:

	def __init__(self):
		self.single = []
		self.overlaps = []

	def book(self, start: int, end: int) -> bool:

		if not self.single:
			self.single += [(start, end)]
			return True
		else:
			for t in self.overlaps:
				if start < t[1] and end > t[0]: # find more conflicts, return False
					return False

			for t in self.single:
				if start < t[1] and end > t[0]:
					self.overlaps += [(max(start, t[0]), min(end, t[1]))] # add overlapped range
			self.single += [(start, end)]
			return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)