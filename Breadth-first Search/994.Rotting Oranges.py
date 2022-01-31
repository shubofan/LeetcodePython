import collections
from typing import List


class Solution:
    # Time O(MN), each cell will be visted once
    # Space O(MN), 2-D array of dist
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]

        fresh = 0
        q = collections.deque()
        # Distance [x][y] means the min take gird[x][y] become rotten if grid[x][y] == 1 i.e. it is a gresh orange
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fresh += 1
                    # for fresh orange, it takes infinate time to be rotten
                    dist[x][y] = float('inf')
                if grid[x][y] == 2:
                    q.append((x, y))

        # no fresh orange, return 0
        if fresh == 0:
            return 0

        # BFS from all rotten oranges
        time_elapsed = 1
        seen = set()
        while q:
            size = len(q)
            while size > 0:
                cur_x, cur_y = q.popleft()
                dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                for d in dirs:
                    next_x, next_y = cur_x + d[0], cur_y + d[1]
                    if 0 <= next_x < m and 0 <= next_y < n and (next_x, next_y) not in seen and grid[next_x][next_y] == 1:
                        seen.add((next_x, next_y))
                        q.append((next_x, next_y))
                        grid[next_x][next_y] = 2
                        dist[next_x][next_y] = min(dist[next_x][next_y], time_elapsed)
                size -= 1
            time_elapsed += 1

        age = -float('inf')
        for x in range(m):
            for y in range(n):
                # the orange can not be rotten
                if dist[x][y] == float('inf'):
                    return -1
                elif dist[x][y] > 0:
                    age = max(age, dist[x][y])

        return age
