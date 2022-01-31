# Time: NlogK
# Space: O(N+K) to store the hash map with not more N elements and a heap with k elements.

from collections import Counter
import heapq
from typing import List


class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		cnt = Counter(nums)
		pq = []
		# N log k
		for num, fre in cnt.items():
			heapq.heappush(pq, (fre, num))
			if len(pq) > k:
				heapq.heappop(pq)
		res = []

		# K log K
		while pq:
			res += [heapq.heappop(pq)[1]]

		return res