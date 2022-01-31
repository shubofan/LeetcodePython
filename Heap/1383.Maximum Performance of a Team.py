# Time O(NlogN) for sorting
# Time O(NlogK) for priority queue
# Space O(N)


import heapq


class Solution:
	def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

		people = []

		for i in range(n):
			people += [(speed[i], efficiency[i])]

		people.sort(key=lambda x: -x[1])

		pq = []
		res = 0
		speed_sum = 0
		for i in range(n):  # For each person(people[i]), it has minimum efficiency
			while len(pq) >= k:  # pop the person with the lowest speed necessary
				person = heapq.heappop(pq)[1]
				speed_sum -= person[0]

			heapq.heappush(pq, (people[i][0], people[i]))
			speed_sum += people[i][0]
			res = max(res, people[i][1] * speed_sum)  # speed is descending , so people[i][1] is always min speed

		return res % (10 ** 9 + 7)