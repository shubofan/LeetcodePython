from typing import List


class Solution:
	# 200 个点能多能封闭多大的空间，如下所示：

	# 0th      _________________________
	#          |O O O O O O O X
	#          |O O O O O O X
	#          |O O O O O X
	#          |O O O O X
	#          .O O O X
	#          .O O X
	#          .O X
	# 200th    |X

	# area: 1 + 2 + .... 199 = (200) * 199 / 2 = 19900

	# 那么就是说若当前能够遍历到 19900 个点，则说明很大机会可以到达终点。当然极端情况下，终点可能被四个黑名单的上的点犹如围棋围杀般的包围着，所以说还需要反着遍历一般，从终点遍历点，若能在 20000 步内到达，或者达到了 20000 步，都返回 true，否则返回 false。

	def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
		if not blocked:
			return True

		blockedSet = set()
		for b in blocked:
			blockedSet.add((b[0], b[1]))

		def bfs(blockedSet, source, target):
			dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
			x, y = source[0], source[1]
			seen = set()
			seen.add((x, y))

			q = collections.deque()
			q += [(x, y)]

			while q:

				x, y = q.popleft()
				# print([x, y], target)
				if [x, y] == target:
					return True
				if len(seen) > 19900:  # area
					return True
				for d in dirs:
					x_next, y_next = x + d[0], y + d[1]

					if 0 <= x_next < 10 ** 6 and 0 <= y_next < 10 ** 6 and (x_next, y_next) not in seen and (
					x_next, y_next) not in blockedSet:
						seen.add((x_next, y_next))
						q += [(x_next, y_next)]

			return False

		return bfs(blockedSet, target, source) and bfs(blockedSet, source, target)