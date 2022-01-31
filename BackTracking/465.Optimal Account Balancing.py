import collections


class Solution:
	"""
	@param edges: a directed graph where each edge is represented by a tuple
	@return: the number of edges
	"""

	def balanceGraph(self, edges):
		dic = collections.defaultdict(int)
		for edge in edges:
			p1, p2, amount = edge[0], edge[1], edge[2]
			dic[p1] -= amount
			dic[p2] += amount

		self.res = float('inf')
		balance = [amount for amount in dic.values() if amount != 0]

		def dfs(balance, start, trans):
			# print(balance)
			n = len(balance)


			# current transaction needed more the res, stop dfs. Prune
			if trans >= self.res:
				return

				# current balance is 0, so move forward
			while start < n and balance[start] == 0:
				start += 1

			# all the balance settled, update res
			if start == n:
				self.res = min(self.res, trans)
				return

			for j in range(start + 1, n):
				# transfer all balance[start] to balance[j]
				if balance[start] * balance[j] < 0:
					balance[j] += balance[start]
					dfs(balance, start + 1, trans + 1)
					# back tracking
					balance[j] -= balance[start]

		dfs(balance, 0, 0)

		return self.res
if __name__ == '__main__':
	s = Solution()
	print(s.balanceGraph([[7,6,1],[4,6,59],[8,9,46],[7,5,92],[14,13,92],[2,1,93],[9,8,19],[14,13,72],[9,8,68],[12,16,4],[14,15,74],[1,3,54],[3,0,63],[5,7,24],[5,6,17],[12,14,89],[8,10,65],[2,1,91],[6,5,94],[1,3,85],[8,10,77],[15,16,40],[11,9,39],[10,9,42],[7,6,5],[9,10,74],[9,8,73],[9,8,87],[9,8,56],[12,16,32],[2,1,25],[10,11,92],[14,15,84],[5,6,22],[2,1,69],[3,2,56],[11,8,38],[3,1,3],[11,8,75],[0,1,49]]))