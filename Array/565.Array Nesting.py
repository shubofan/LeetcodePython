from typing import List


class Solution:

	# Time complexity : O(n) Every element of the nums. array will be considered atmost once.

	# Space complexity : O(n) visited array of size n is used.
	def arrayNesting(self, nums: List[int]) -> int:
		res = 0
		# if a number has been visited
		visited = set()
		for i, num in enumerate(nums):
			# try to find the largest circle
			if num not in visited:
				count = 0
				start = num
				visited.add(start)
				while True:
					count += 1
					start = nums[start]
					if start in visited:
						break
					else:
						visited.add(start)

				res = max(res, count)
		return res