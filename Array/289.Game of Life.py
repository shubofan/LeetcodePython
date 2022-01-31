from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                cnt = self.check(board, i, j)
                # die -> live
                if board[i][j] == 0 and cnt == 3:
                    board[i][j] = 2
                # live -> die
                if board[i][j] == 1 and (cnt > 3 or cnt < 2):
                    board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                if board[i][j] <= 0:
                    board[i][j] = 0

    def check(self, board: List[List[int]], x: int, y: int) -> bool:
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
        m, n = len(board), len(board[0])
        cnt = 0
        for direction in directions:
            x_next, y_next = x + direction[0], y + direction[1]
            # if the original status of (x_next, y_next) is live
            if 0 <= x_next < m and 0 <= y_next < n and (board[x_next][y_next] == 1 or board[x_next][y_next] == -1):
                cnt += 1

        return cnt
