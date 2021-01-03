class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        if m == 1 or n == 1:
            return

        # Search each node in the edges
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(0, j, board)
            if board[m - 1][j] == 'O':
                self.dfs(m - 1, j, board)

        for i in range(m - 1):
            if board[i][0] == 'O':
                self.dfs(i, 0, board)
            if board[i][n - 1] == 'O':
                self.dfs(i, n - 1, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'Z':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

    def dfs(self, i, j, board):
        if 0 <= i < len(board) and 0 <= j < len(board[i]) and board[i][j] == 'O':
            # mark position in z so the the original O to be kept
            board[i][j] = 'Z'
            self.dfs(i + 1, j, board)
            self.dfs(i - 1, j, board)
            self.dfs(i, j + 1, board)
            self.dfs(i, j - 1, board)
        else:
            return
