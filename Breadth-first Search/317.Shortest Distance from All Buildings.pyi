from collections import deque


class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """

    def shortestDistance(self, grid):
        m, n = len(grid), len(grid[0])

        buildings = []
        # total distance to certain empty place from all buildings
        self.dist = [[0] * n for _ in range(m)]
        # key is the position of empty space, value is the number of buildings can reach from this empty place
        self.reached = {}

        # Time O(M^2*N^2)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += [(i, j)]

        for building in buildings:
            self.bfs(grid, building, set())

        res = float('inf')
        for i in range(m):
            for j in range(n):
                # if all the building can reach this empty 
                if self.dist[i][j] != 0 and self.reached[(i, j)] == len(buildings):
                    res = min(self.dist[i][j], res)

        return res

    # each BSF takes O(MN) since it need to search entire grid
    def bfs(self, grid, building, seen):
        m, n = len(grid), len(grid[0])
        x, y = building[0], building[1]
        seen.add((x, y))

        q = deque()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q += [(x, y, 0)]

        while q:
            x, y, dis = q.popleft()
            self.dist[x][y] += dis

            for d in dirs:
                x_next, y_next = x + d[0], y + d[1]
                if 0 <= x_next < m and 0 <= y_next < n and (x_next, y_next) not in seen:
                    seen.add((x_next, y_next))
                    if grid[x_next][y_next] == 0:
                        self.reached[(x_next, y_next)] = self.reached.get((x_next, y_next), 0) + 1
                        q += [(x_next, y_next, dis + 1)]