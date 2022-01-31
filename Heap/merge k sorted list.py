import heapq
from typing import List


class Solution:
    def merge(self, lists: List[List[int]]) -> List[int]:
        res = []
        pq = []
        for i, lst in enumerate(lists):
            heapq.heappush(pq, (lst[0], i))

        while pq:
            element, idx = heapq.heappop(pq)
            res += [element]
            lists[idx].pop(0)
            if lists[idx]:
                heapq.heappush(pq, (lists[idx][0], idx))
        return res


if __name__ == '__main__':
    lst = [[1,2,3], [2,3,4], [0,1]]
    s = Solution()
    print(s.merge(lst))

