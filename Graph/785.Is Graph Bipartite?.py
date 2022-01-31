import collections
# 我们任选一个节点开始，将其染成红色，并从该节点开始对整个无向图进行遍历；
#
# 在遍历的过程中，如果我们通过节点 u 遍历到了节点 v（即 u 和 v 在图中有一条边直接相连），那么会有两种情况：
#
#     如果 v 未被染色，那么我们将其染成与 u 不同的颜色，并对 v 直接相连的节点进行遍历；
#
#     如果 v 被染色，并且颜色与 u 相同，那么说明给定的无向图不是二分图。我们可以直接退出遍历并返回 False 作为答案。
#
# 当遍历结束时，说明给定的无向图是二分图，返回 True。

# Time : O(N+E), n is the number of vertices and e is the number of edges
# Space : O(N+E), n is the number of vertices and e is the number of edges
from typing import List


class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		g = collections.defaultdict(set)
		self.visited = set()
		n = len(graph)
		for i in range(n):
			nbrs = graph[i]
			for nbr in nbrs:
				g[i].add(nbr)
		# Two different colors (True, False)
		self.colors = {}
		for i in range(n):
			if i not in self.visited:
				if not self.dfs(g, i, False):
					return False
		return True

	def dfs(self, g, i, color):
		self.visited.add(i)
		self.colors[i] = color
		for nbr in g[i]:
			if nbr not in self.visited:
				if not self.dfs(g, nbr, not color):
					return False
			else:
				if self.colors[nbr] == color:
					return False
		return True
