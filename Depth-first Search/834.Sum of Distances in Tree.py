# Time: Overall  take O(N). Build graph, pre_order, post_order take (N) respectively,
# Space: O(N)

class Solution:
	def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
		self.g = collections.defaultdict(set)
		for e in edges:
			self.g[e[0]].add(e[1])
			self.g[e[1]].add(e[0])

		# res[i]: total distance to all node from i
		self.res = [0] * n

		# cnt[i]: node i itself plus all its descendants
		self.cnt = [1] * n

		# 1. calculate this correct cnt[i]
		# 2. res[i] is the total distance from i to all its descendants
		def post_order(node, parent):
			for child in self.g[node]:
				if child != parent:
					post_order(child, node)
					self.cnt[node] += self.cnt[child]
					self.res[node] += self.res[child] + self.cnt[child]

		# for res[i] add distance from i to all its nodes that are not its descendants
		def pre_order(node, parent):
			n = len(self.cnt)
			for child in self.g[node]:
				if child != parent:
					# 与 node 相比(res[node])， we have cnt[child] 个 nodes are 1 closer to child
					# 与 node 相比(res[node])， we have (n - self.cnt[child] 个 nodes are 1 further to child
					self.res[child] = self.res[node] - self.cnt[child] * 1 + (n - self.cnt[child]) * 1
					pre_order(child, node)

		post_order(0, -1)
		pre_order(0, -1)
		return self.res