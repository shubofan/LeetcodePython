import heapq


class Solution:
	def maxEvents(self, events: List[List[int]]) -> int:
		# O(nlogn)
		events.sort(key=lambda x: (x[0], x[1]))
		res = 0
		day = 1
		i = 0  # track the array

		pq = []  # add end day for each event to pq

		while pq or i < len(events):
			# today has missed the end day of top event in pq
			while pq and pq[0] < day:
				heapq.heappop(pq)

			# events[i] can be attended
			while i < len(events) and events[i][0] <= day:
				heapq.heappush(pq, events[i][1])
				i += 1

			# attend events[0]
			if pq:
				heapq.heappop(pq)
				res += 1
			day += 1
		return res