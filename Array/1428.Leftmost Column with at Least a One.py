class Solution:
	"""
	@param arr: The 2-dimension array
	@return: Return the column the leftmost one is located
	"""

	# Search from right up corner
	# Time: O(M + N), walk a diagonal
	def getColumn(self, arr):
		m, n = len(arr), len(arr[0])
		i, j = 0, n - 1
		while i < m and j >= 0:
			if arr[i][j] == 1:
				j -= 1
			else:
				i += 1

		return j + 1