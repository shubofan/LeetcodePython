import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # max_v is the max value we visited so far
        l, r, max_v = 0, float('inf'), max(vec[0] for vec in nums)

        # min heap so that we can ensure each time pop element with minimum value
        pq = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(pq)

        while True:
            val, row, idx = heapq.heappop(pq)
            # update l and r, if current range is smaller
            if max_v - val < r - l:
                l = val
                r = max_v
            # if we reached end of certain list, we stop because heap will never have element in this list
            if idx == len(nums[row]) - 1:
                break
            # nums[row][idx+1] is the element to be pushed into heap, so update max_v accoardingly
            max_v = max(max_v, nums[row][idx + 1])
            heapq.heappush(pq, (nums[row][idx + 1], row, idx + 1))

        return [l, r]
