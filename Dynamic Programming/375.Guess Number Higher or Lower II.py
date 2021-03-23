class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[float('inf')] * (n + 1) for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][i] = 0

        for j in range(2, n + 1):
            for i in range(j - 1, 0, -1):
                for k in range(i + 1, j):  # assume guess k and k != i and k != j
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))
                # assume guess k and k == i
                dp[i][j] = min(dp[i][j], i + dp[i + 1][j]);
                # assume guess k and k == j
                dp[i][j] = min(dp[i][j], j + dp[i][j - 1]);

        return dp[1][n]
