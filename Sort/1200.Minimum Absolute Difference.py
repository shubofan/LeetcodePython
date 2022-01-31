from typing import List


class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		arr.sort()
		n = len(arr)
		res = []

		diff = float('inf')
		for i in range(n - 1):
			if arr[i + 1] - arr[i] < diff:
				res = [[arr[i], arr[i + 1]]]
				diff = arr[i + 1] - arr[i]
			elif arr[i + 1] - arr[i] == diff:
				res += [[arr[i], arr[i + 1]]]

		return res