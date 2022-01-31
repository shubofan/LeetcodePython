# class Solution:
#     def countBattleships(self, board: List[List[str]]) -> int:
#         m, n = len(board), len(board[0])
#         res = 0
#         for x in range(m):
#             for y in range(n):
#                 if board[x][y] == 'X':
#                     self.dfs(board, x, y)
#                     res +=1
#         return res

#     def dfs(self, board: List[List[str]], x:int, y:int) -> None:
#         if  x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
#             return
#         if board[x][y] == 'X':
#             board[x][y] = '.'
#             self.dfs(board, x + 1, y)
#             self.dfs(board, x - 1, y)
#             self.dfs(board, x, y + 1)
#             self.dfs(board, x, y - 1)

# Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
class Solution:
	def countBattleships(self, board: List[List[str]]) -> int:
		res = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == '.':
					continue
				if i > 0 and board[i - 1][j] == 'X':
					continue
				if j > 0 and board[i][j - 1] == 'X':
					continue
				res += 1
		return res