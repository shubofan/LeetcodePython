from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf') for i in range(n)] for j in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0

        while q:
            x, y = q.popleft()

            i = x + 1
            if i < m and dist[i][y] > dist[x][y] + 1:
                dist[i][y] = dist[x][y] + 1
                q.append((i, y))

            i = x - 1
            if i >= 0 and dist[i][y] > dist[x][y] + 1:
                dist[i][y] = dist[x][y] + 1
                q.append((i, y))

            i = y + 1
            if i < n and dist[x][i] > dist[x][y] + 1:
                dist[x][i] = dist[x][y] + 1
                q.append((x, i))

            i = y - 1
            if i >= 0 and dist[x][i] > dist[x][y] + 1:
                dist[x][i] = dist[x][y] + 1
                q.append((x, i))

        return dist
