from collections import defaultdict
from typing import List


class Solution:
	# Let N be the number of input equations and M be the number of queries.
	def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		# build a graph
		self.g = defaultdict(set)

		# build a wight dic, (x,y) = w1, (y,x) = 1/w1
		self.w = defaultdict(float)
		res = []
		for i, e in enumerate(equations):
			x, y = e[0], e[1]
			self.g[x].add(y)
			self.g[y].add(x)
			weight = values[i]

			self.w[(x, y)] = weight
			self.w[(y, x)] = 1.0 / weight
		# For each query, it may traverse entire graph that takes O(N) .
		# Hence, in total, the evaluation of queries could take M⋅(N)=(M⋅N).
		for q in queries:
			if q[0] not in self.g or q[1] not in self.g:
				res += [-1.0]
			else:
				res += [self.search(q[0], q[1], 1.0, set())]
		return res

	# Search if there is a path from x, y, take O(M)
	def search(self, x, y, weight, visited):
		res = weight

		# found a path from x to y !
		if x == y:
			return res
		visited.add(x)
		for nbr in self.g[x]:
			if nbr not in visited:
				res = self.search(nbr, y, weight * self.w[(x, nbr)], visited)
				# find a path, return res
				if res != -1.0:
					return res
		# did not find a path, return -1.0
		return -1.0


