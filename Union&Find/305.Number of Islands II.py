"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

"""
Time complexity : O(m×n+L) where L is the number of operations, m is the number of rows and n is the number of columns. it takes O(m×n) to initialize UnionFind, and O(L)

to process positions. Note that Union operation takes essentially constant time ^1 when UnionFind is implemented with both path compression and union by rank.

Space complexity : O(m×n)
as required by UnionFind data structure. 


"""

# 伪代码
# for i 1:n
#   fa[i]=i   //伪代码，一开始让所有的父亲都是本身
#             //我们规定代表元的父亲为本身，如果一个节点的父亲不是本身，说是它在一个元素个数大于1的集合中，而且这个节点并不是代表元

# function find(x)  //寻找x所在集合的代表元
#   if(fa[x]==x)
#     return x;  //x是代表元，直接返回
#   else
#     return fa[x]=find(fa[x]) //x不是代表元，寻找x的父亲的代表元是谁，并且直接把代表元赋值给x的父亲

#  function union（x,y）//合并两个集合
#    fa[find(x)]=find(y)

class UnionFind:
	def __init__(self):
		self.parent = {} # <(x, y), parent>
		self.count = 0 # number of dis-join set

	def init(self, x):
		if x not in self.parent:
			self.parent[x] = x
			self.count += 1

	def find(self, x):
		if x == self.parent[x]:
			return x
		self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		rootX, rootY = self.find(x), self.find(y)
		if rootX == rootY:
			return
		self.parent[rootX] = rootY
		self.count -= 1

	def getNumIslands(self):
		return self.count


class Solution:
	def numIslands2(self, m, n, positions):
		res = []
		board = [[0] * n for _ in range(m)]
		uf = UnionFind()

		for point in positions:
			x, y = point.x, point.y
			board[x][y] = 1
			uf.init((x, y))

			for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
				nx, ny = x + dx, y + dy
				if not 0 <= nx < m or not 0 <= ny < n:
					continue
				if board[nx][ny] == 1:
					uf.union((x, y), (nx, ny))

			res.append(uf.getNumIslands())

		return res