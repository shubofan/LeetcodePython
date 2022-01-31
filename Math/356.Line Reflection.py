class Solution:
	"""
	@param points: n points on a 2D plane
	@return: if there is such a line parallel to y-axis that reflect the given points
	"""

	def isReflected(self, points):
		if not points:
			return True
		max_x = -float('inf')
		min_x = float('inf')

		# make the set of points tuple
		p_s = set()
		for point in points:
			p_s.add((point[0], point[1]))
			max_x = max(point[0], max_x)
			min_x = min(point[0], min_x)

		# The x value for a point and its corresponding point sums to a fixed value,
		# which can be obtained by summing the min x value and max x value.
		sum_x = max_x + min_x

		for point in points:
			x, y = point[0], point[1]
			reflected_point = (sum_x - x, y)
			if reflected_point not in p_s:
				return False
		return True