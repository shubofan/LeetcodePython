from typing import List


class Solution:
    # Time complexity : O(mn).
    # Each vertex/cell will be calculated once and only once, and each edge will be visited once and only once.
    # The total time complexity is then O(V+E). V is the total number of vertices and E is the total number of edges. In our problem, O(V)=O(mn), O(E)≈O(4mn)=O(mn)

    # Space complexity : O(mn)
    # The cache dominates the space complexity.
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        # mem[x][y] means the Longest Increasing Path from matrix[x][y]
        self.mem = [[1] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                res = max(res, self.dfs(matrix, x, y))
        return res

    def dfs(self, matrix, x, y) -> None:
        if self.mem[x][y] > 1:
            return self.mem[x][y]

        m, n = len(matrix), len(matrix[0])
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        for d in dirs:
            x_next, y_next = x + d[0], y + d[1]
            if 0 <= x_next < m and 0 <= y_next < n and matrix[x_next][y_next] > matrix[x][y]:
                self.mem[x][y] = max(self.mem[x][y], self.dfs(matrix, x_next, y_next) + 1)
        return self.mem[x][y]
