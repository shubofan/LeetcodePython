from typing import List

# each element enqueue at least one time , and dequeue if necessary, so time complexity should be O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        # monotone decrease stack
        for i in range(n):
            # current ith day is the first day warmer than the day on the top of stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack += [i]

        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # monotone decrease stack
        for i, temperature in enumerate(temperatures):
            # current ith day is the first day warmer than the day on the top of stack
            while stack and stack[-1][1] < temperature:
                idx, tem = stack.pop()
                res[idx] = i - idx
            stack += [(i, temperature)]
        return res




