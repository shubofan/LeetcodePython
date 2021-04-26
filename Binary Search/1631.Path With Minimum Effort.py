from collections import deque
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # possible effort[l, r]
        l, r = 0, 10** 6 - 1
        m, n = len(heights), len(heights[0])
        while l < r:
            mid = (l + r) // 2
            visited = set()
            visited.add((0,0))
            queue = deque()
            queue += [(0,0)]
            # BFS from (0, 0)
            while queue:
                x, y = queue.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0<= nx <= m - 1 and 0<= ny <= n - 1 and (nx, ny) not in visited and abs(heights[x][y] - heights[nx][ny]) <= mid :
                        queue += [(nx, ny)]
                        visited.add((nx, ny))
            # if can reach (m-1, n-1), try to find the min effort from left half
            if (m - 1, n - 1) in visited:
                r = mid
            # try to find the min effort from left half
            else:
                l = mid + 1
        return l