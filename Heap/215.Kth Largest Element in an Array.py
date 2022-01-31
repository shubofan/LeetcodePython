# Time O(nlogK)
# Space O(K)
import heapq


class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		pq = []
		for num in nums:
			heapq.heappush(pq, num)
			# pop (n -k) smallest elements, so that the top of heap is the Kth largest num
			if len(pq) > k:
				heapq.heappop(pq)
		return pq[0]
