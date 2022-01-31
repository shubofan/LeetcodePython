class MyCalendar:

	def __init__(self):
		self.c = []

	def book(self, start: int, end: int) -> bool:
		for event in self.c:
			if start < event[1] and end > event[0]:
				return False
		self.c += [(start, end)]
		return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)