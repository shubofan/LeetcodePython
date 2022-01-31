from typing import List


class Solution:
	def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
		def get_dis_squar(p1, p2):
			return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

		points = [p1, p2, p3, p4]
		points.sort(key=lambda p: (p[0], p[1]))
		p0, p1, p2, p3 = points[0], points[1], points[2], points[3]

		# get_dis_squar(p0, p1) != 0 -> no same point
		# get_dis_squar(p0, p1) == get_dis_squar(p0, p2) -> 4 edges same length
		# get_dis_squar(p0, p3) == get_dis_squar(p1, p2) -> length of diagnals same length
		return get_dis_squar(p0, p1) != 0 and get_dis_squar(p0, p1) == get_dis_squar(p0, p2) and get_dis_squar(p0,p3) == get_dis_squar(p1, p2)