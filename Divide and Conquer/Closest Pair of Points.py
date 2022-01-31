class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# T(n)=2T(n/2)+O(n)+O(nlogn) +O(n),
#T(n)=2T(n/2)+O(nlogn) ---->nlogn -> 		points3.sort(key=lambda p: p.y)
# T(n)=O(n*logn*logn)

# https://www.jianshu.com/p/8bc681afbaff
class Closest:
	def dist(self, p1, p2):
		return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

	def get_closest_pair(self, points):
		dist = lambda p1, p2: ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

		n = len(points)
		if n == 1:
			return float('inf')
		if n == 2:
			return dist(points[0], points[1])

		points.sort(key=lambda p: p.x) #根据x坐标从小到大排序

		mid_x = points[n//2].x
		# print(mid_x)
		l =  points[:n//2] # 分治求解左半部分子集的最近点
		r = points[n//2:] # 分治求解右半部分子集的最近点
		# print(len(l)),
		# print(len(r))
		d1, d2 = self.get_closest_pair(l), self.get_closest_pair(r)

		d = min(d1, d2) # 记录最近距离

		# 取得中线2d宽度的所有点
		points3 = []
		for point in points:
			if abs(point.x - mid_x) <= d:
				points3 += [point]

		#  以y排序矩形阵内的点集合
		points3.sort(key=lambda p: p.y)

		for i in range(len(points3)):
			for j in range(i + 1, len(points3)):
				if points3[j].y - points3[i].y >= d:
					continue
				d = min(dist(points3[i], points3[j]), d) # 如果亮点的距离在d以内， 更新最小距离

		return d

if __name__ == '__main__':
	c = Closest()
	P = [Point(2, 3), Point(12, 30),
	     Point(40, 50), Point(5, 1),
	     Point(12, 10), Point(3, 4)]

	print("The smallest distance is",
	      c.get_closest_pair(P))

	P2 = [Point(1, 4), Point(1, 8),
	     Point(2, 1), Point(3, 2),
	     Point(4, 4), Point(5, 1),
	     Point(7, 2), Point(6, 6)]
	print("The smallest distance is",
	      c.get_closest_pair(P2))