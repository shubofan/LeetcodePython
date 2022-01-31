import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        points = []

        for build in buildings:
            points += [(build[0], build[2])]  # left corner
            points += [(build[1], -1 * build[2])]  # right corner, if height is negative, so that it is the right corner

        points = sorted(points, key=lambda x: (x[0], -x[1]))

        # maintain a max heap
        heap = [0]
        max_h = 0

        for point in points:
            # current point is left corner point, add to max heap
            if point[1] > 0:
                heapq.heappush(heap, -point[1])
            # current point is right corner point, remove it from heap
            else:
                heap.remove(point[1])
                heapq.heapify(heap)

            # current max height
            top = -heap[0]
            # if max height changed, So we NEED to add it to the res
            if top != max_h:
                res += [[point[0], top]]
                max_h = top

        return res