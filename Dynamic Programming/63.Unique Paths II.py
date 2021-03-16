from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for i in range(n)] for j in range(m)]

        # dp[i][j] means that # of ways from [0, 0] to [i, j]

        for i in range(n):
            # meet a obstacleGrid, set it to 0 and all the grid after it to 0
            if obstacleGrid[0][i]:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1

        for i in range(m):
            # meet a obstacleGrid, set it to 0 and all the grid after it to 0
            if obstacleGrid[i][0]:
                dp[i][0] = 0
                break
            else:
                dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
