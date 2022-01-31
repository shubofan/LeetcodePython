#     Time: O(M * N), where M <= 50 is number of rows, N <= 50 is number of columns in the matrix.
#     Space: O(M * N), it's the depth stack memory, in worst case is O(M * N), can check this discussion: https://stackoverflow.com/a/50912382/4084297


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        q = collections.deque()
        seen = set()
        seen.add((sr, sc))
        q += [(sr, sc)]

        old_color = image[sr][sc]
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        while q:
            x, y = q.popleft()
            image[x][y] = newColor
            for d in dirs:
                nx,ny = x + d[0], y + d[1]
                if 0<= nx < m and 0<= ny < n and (nx, ny) not in seen and image[nx][ny] == old_color:
                    seen.add((nx, ny))
                    q += [(nx, ny)]
        return image

# DFS

#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         m, n = len(image), len(image[0])

#         def dfs(x, y, old_color):

#             if x < 0 or x >= m or y < 0 or y >= n:
#                 return
#             if image[x][y] == newColor or image[x][y] != old_color:
#                 return
#             image[x][y] = newColor

#             dfs(x+1, y, old_color)
#             dfs(x-1, y, old_color)
#             dfs(x, y+1, old_color)
#             dfs(x, y-1, old_color)

#         dfs(sr, sc, image[sr][sc])
#         return image