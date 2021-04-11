from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        res = 0

        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                res = max(res, dp[i + 1][j + 1])
        return res
