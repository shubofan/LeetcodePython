from typing import List


class Solution:

    def __init__(self):
        self.res = []

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])

        # assume all node cannot flow to atl or pac
        pac = [[False for i in range(n)] for j in range(m)]
        alt = [[False for i in range(n)] for j in range(m)]

        # DFS from pac and alt, mark pac[i][j] to True if pac can flow to matrix[i][j].
        for i in range(m):
            self.dfs(matrix, pac, i, 0)
            self.dfs(matrix, alt, i, n - 1)

        for j in range(n):
            self.dfs(matrix, pac, 0, j)
            self.dfs(matrix, alt, m - 1, j)

        for i in range(m):
            for j in range(n):
                if (pac[i][j] and alt[i][j]):
                    self.res += [[i, j]]
        return self.res

    def dfs(self, matrix: List[List[int]], visited: List[List[bool]], i: int, j: int) -> None:
        visited[i][j] = True

        x, y = i, j + 1
        if not (x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or visited[x][y] or matrix[i][j] > matrix[x][
            y]):
            self.dfs(matrix, visited, x, y)

        x, y = i, j - 1
        if not (x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or visited[x][y] or matrix[i][j] > matrix[x][
            y]):
            self.dfs(matrix, visited, x, y)

        x, y = i - 1, j
        if not (x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or visited[x][y] or matrix[i][j] > matrix[x][
            y]):
            self.dfs(matrix, visited, x, y)

        x, y = i + 1, j
        if not (x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or visited[x][y] or matrix[i][j] > matrix[x][
            y]):
            self.dfs(matrix, visited, x, y)
