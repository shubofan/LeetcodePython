"""
Time complexity is constant here since the board size is fixed and there is no N-parameter to measure.



Though let's discuss the number of operations needed : (9!)9. Let's consider one row, i.e. not more than 9 cells to fill.

There are not more than 9 possibilities for the first number to put, not more than 9×8 for the second one, not more than 9×8×7 for the third one etc. In total that results in not more than 9! possibilities for a just one row, that means not more than (9!)^9 operations in total.

Let's compare:

    9^81=196627050475552913618075908526912116283103450944214766927315415537966391196809 for the brute force, and (9!)^9=109110688415571316480344899355894085582848000000000
for the standard backtracking, i.e. the number of operations is reduced in 10^27 times !



Space complexity : the board size is fixed, and the space is used to store board, rows, columns and boxes structures, each contains 81 elements

"""
from typing import List


class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""

		def solve(board):
			nums = [str(i) for i in range(1, 10)]

			for i in range(9):
				for j in range(9):
					if board[i][j] == '.':
						for num in nums:
							if self.isValidPlace(board, i, j, num):  # place num to board[i][j]
								board[i][j] = num
								if solve(board):
									return True
								board[i][j] = '.'  # backTracking
						return False

			return True

		solve(board)

	def isValidPlace(self, board: List[List[str]], x: int, y: int, num: int) -> bool:
		regionRow = (x // 3) * 3
		regionCol = (y // 3) * 3

		for i in range(9):
			if board[x][i] == num or board[i][y] == num:
				return False
			if board[regionRow + i // 3][regionCol + i % 3] == num:
				return False

		return True