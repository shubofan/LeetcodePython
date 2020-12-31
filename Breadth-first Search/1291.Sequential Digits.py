from collections import deque
from typing import List


class Solution:
    # Back tracking
    #     def sequentialDigits(self, low: int, high: int) -> List[int]:
    #         self.res = []
    #         self.low = low
    #         self.high = high
    #         size_low = len(str(low))
    #         size_high = len(str(high))

    #         for l in range(size_low, size_high + 1):
    #             for k in range(1, 10 - l + 1):
    #                 self.getDigits(l, str(k))
    #         return self.res

    #     def getDigits(self, n: int, path: str):
    #         if len(path) == n and int(path) <= self.high and int(path) >= self.low:
    #             self.res += [path]
    #             return
    #         last_digit = int(path[-1])
    #         if last_digit < 9:
    #             self.getDigits(n, path + str(last_digit + 1))

    # BFS
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque()
        for i in range(1, 10):
            queue += [i]

        res = []
        while queue:
            top = queue.popleft()
            if low <= top <= high:
                res += [top]

            lst_digit = int(str(top)[-1])
            if lst_digit != 9:
                queue += [int(str(top) + str(lst_digit + 1))]
        return res
