from typing import List

# DFS
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
            grid[i][j] = '2' # marked cell to 2, so it will not be visited again
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)
# BFS
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m , n = len(grid), len(grid[0])

#         res = 0
#         dirc = [[-1,0],[1,0], [0,-1], [0,1]]

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     res += 1
#                     q = deque()
#                     q += [(i, j)]
#                     grid[i][j] = 'x'
#                     while q:
#                         x, y = q.popleft()
#                         for d in dirc:
#                             x_next, y_next = x + d[0], y + d[1]
#                             if 0<= x_next < m and 0<= y_next < n and grid[x_next][y_next] == '1':
#                                 q += [(x_next, y_next)]
#                                 grid[x_next][y_next] = 'x'
#         return res