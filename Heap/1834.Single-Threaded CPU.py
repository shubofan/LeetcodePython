import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        if not tasks:
            return res
        pq = []
        i = 0

        tasks = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        tasks.sort()
        cur_time = tasks[0][0]

        while len(res) < len(tasks):
            # if enqueueTime <= current time, put task in pq. (sorted by process Time)
            while i < len(tasks) and tasks[i][0] <= cur_time:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1

            if pq:
                # deque and update current time
                time, original_idx = heapq.heappop(pq)
                res += [original_idx]
                cur_time += time
            elif i < len(tasks): # pq is empty
                cur_time = tasks[i][0]
        return res
