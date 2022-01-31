"""
时间复杂度：令路线的数量为 n，车站的个数为 m。建图的时间复杂度为 O(∑i=0n−1 len(rs[i]))；
BFS 部分每个路线只会入队一次，最坏情况下每个路线都包含所有车站, 复杂度为 O(n∗m)。整体复杂度为 O(n∗m + ∑i=0 to n−1 len(routes[i]))
空间复杂度：O(n∗m)
"""

import collections

import  random
class Solution(object):
	def numBusesToDestination(self, routes, source, target):
		"""
		:type routes: List[List[int]]
		:type source: int
		:type target: int
		:rtype: int
		"""
		g = collections.defaultdict(set)  # <stop, [idx of bus route]>

		for i, route in enumerate(routes):
			for stop in route:
				g[stop].add(i)

		# all the routes visited
		seen = set()

		q = collections.deque()
		q += [(source, 0)]

		while q:
			node, level = q.popleft()
			if node == target:
				return level

			for bus_route in g[node]:
				if bus_route in seen:
					continue
				seen.add(bus_route)
				for stop in routes[bus_route]:  # all the stops can reach in current bus_route
					q += [(stop, level + 1)]
					random.randint(1,3,2)


		return -1