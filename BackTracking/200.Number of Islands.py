from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        if not grid:
            return self.res

        m, n = len(grid), len(grid[0])

        if m == 0 or n == 0:
            return self.res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '2'
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)