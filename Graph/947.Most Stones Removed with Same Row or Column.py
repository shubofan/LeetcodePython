import collections
"""
 The main insight is that we can always make moves that reduce the number of stones in each component to 1. 
"""

class Solution:
	# Time O(N^2), for each node, run a DFS which take O(N),
	# SpaceO(N^2) , for each N, most (N-1) edges, so totally need O(N) * O(N) to store the graph
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


		self.visited = set()
		num_of_connected_component = 0
		# for each connected component, res + (component.size  - 1)
		for i in range(n):

			if i not in self.visited:
				self.dfs(i)
				num_of_connected_component += 1
		return n - num_of_connected_component

	def dfs(self, i):
		self.visited.add(i)
		for nbr in self.g[i]:
			if nbr not in self.visited:
				self.dfs(nbr)
