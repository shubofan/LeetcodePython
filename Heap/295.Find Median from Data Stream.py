import heapq


class MedianFinder:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.max_heap = []  # 2, 1, 0 the smallest half
		self.min_heap = []  # 3, 4, 5 the largest half

	def addNum(self, num: int) -> None:
		heapq.heappush(self.max_heap, -num)
		heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
		if len(self.max_heap) != len(self.min_heap):
			heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

	def findMedian(self) -> float:
		if len(self.max_heap) == len(self.min_heap):
			return (-self.max_heap[0] + self.min_heap[0]) / 2.0
		else:
			return -self.max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()