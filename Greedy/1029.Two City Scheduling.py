 from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Assume all n people go to b, then n / 2 people need to go to a with Acost - Bcost(can be negative).
        # So we want to pay  sum of (Acost - Bcost) for n/2 people in minimum
        # sorted by Acost - Bcost
        costs.sort(key=lambda x: x[0] - x[1])
        res = 0
        n = len(costs)
        for i in range(n // 2):
            res += costs[i][0]
        for i in range(n // 2, n):
            res += costs[i][1]
        return res