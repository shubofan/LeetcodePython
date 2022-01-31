import heapq


# Max heap. NlogK
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []

        for point in points:
            x, y = point[0], point[1]
            dist = x ** 2 + y ** 2
            heapq.heappush(pq, (-dist, point))
            if len(pq) > k:
                heapq.heappop(pq)

        res = []

        while pq:
            res += [heapq.heappop(pq)[1]]

        return res[::-1]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0]**2 + point[1]**2)
        return points[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)