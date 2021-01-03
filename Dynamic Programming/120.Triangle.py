from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp[i][j] min len from top to [i][j]
        dp = [[float('inf')] * n for i in range(n)]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            # if j = 0, i.e. first element in each row,  dp[i-1][j-1] is not valid
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            for j in range(1, i + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
        return min(dp[-1])
