# Time Complexity: O(N^2), where N is the length of positions . We use two for-loops, each of complexity O(N)

# Space Complexity: O(N)
from typing import List


class Solution:
	def fallingSquares(self, positions: List[List[int]]) -> List[int]:
		n = len(positions)
		height = [0] * n  # height[i] be the maximum height of the interval specified by positions[i]

		for i in range(n):
			position = positions[i]
			l, r, h = position[0], position[0] + position[1], position[1]
			height[i] += h  # accumulative height + its height

			for j in range(i + 1, n):
				position2 = positions[j]
				l2, r2, h2 = position2[0], position2[0] + position2[1], position2[1]

				if r2 > l and l2 < r:  # pos[i], and pos[j] overlapped
					height[j] = max(height[j], height[i])  # height[i] is the accumulative height with all overlaps BUT WITHOUT itself
		res = []

		for h in height:
			if not res:
				res += [h]
			else:
				res += [max(res[-1], h)]
		return res