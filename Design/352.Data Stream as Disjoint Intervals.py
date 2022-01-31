class SummaryRanges:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.intervals = []
		self.seen = set()

	def addNum(self, val: int) -> None:
		if val not in self.seen:
			heapq.heappush(self.intervals, [val, val])

	def getIntervals(self) -> List[List[int]]:
		res = []

		while self.intervals:
			cur = heapq.heappop(self.intervals)
			if res and res[-1][1] + 1 >= cur[
				0]:  # res[-1] = [1, 2] , cur = [3, 5] -> res[-1] = [1, 5], res[-1] = [1, 9] , cur = [3, 5] -> res[-1] = [1, 9]
				res[-1][1] = max(res[-1][1], cur[1])
			else:
				res += [cur]
		self.intervals = res
		return self.intervals

	# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()