import collections
from typing import List


class Solution:
	# Time O(N^2), for each node, run a DFS which take O(N),
	# Space O(N^2) , for each N, most (N-1) edges, so totally need O(N) * O(N) to store the graph

	# 这样我们只需要统计整张图中有多少个极大连通子图（也叫做连通块或连通分量）即可。
	# 最终能够留下来的点的数量，即为连通块的数量。我们用总点数减去连通块的数量，即可知道我们可以删去的点的最大数量


	def removeStones(self, stones: List[List[int]]) -> int:
		self.g = collections.defaultdict(set)
		n = len(stones)
		for i in range(n):
			for j in range(i + 1, n):
				if i != j:
					s1, s2 = stones[i], stones[j]
					if s1[0] == s2[0] or s1[1] == s2[1]:
						self.g[i].add(j)
						self.g[j].add(i)

		res = 0
		self.visited = set()

		# for each connected component, res + (component.size  - 1)
		for i in range(n):
			pre = len(self.visited)
			if i not in self.visited:
				self.dfs(i)
				# (len(self.visited) - pre size of new connected component
				res += (len(self.visited) - pre - 1)
		# print(res)
		return res

	def dfs(self, i):
		self.visited.add(i)
		for nbr in self.g[i]:
			if nbr not in self.visited:
				self.dfs(nbr)
