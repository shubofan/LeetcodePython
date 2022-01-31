# Time complexity: O(n!), space complexity: O(n!).
class Solution:
	def solveNQueens(self, n: int) -> List[List[str]]:
		def backtrack(row):
			if row == n:
				res.append(list(board))

			for col in range(n):
				if col not in cols and col - row not in diag and col + row not in anti_diag:
					cols.add(col)
					diag.add(col - row)
					anti_diag.add(col + row)

					board.append("." * (col) + "Q" + "." * (n - col - 1))
					backtrack(row + 1)

					board.pop()
					anti_diag.remove(col + row)
					diag.remove(col - row)
					cols.remove(col)

		res = []
		board = []
		cols = set()
		diag = set()
		anti_diag = set()
		backtrack(0)
		return res


