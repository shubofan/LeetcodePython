import collections


# Time O(M * N)
# Space O(N) set may take  m * n tuples
class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		l1, l2 = len(s1), len(s2)
		l3 = len(s3)
		if l1 + l2 != l3:
			return False
		visited = set()
		q = collections.deque()
		q += [(0, 0)]

		while q:
			x, y = q.popleft()

			if x == l1 and y == l2:
				return True
			if x < l1 and s1[x] == s3[x + y] and (x + 1, y) not in visited:
				q += [(x + 1, y)]
				visited.add((x + 1, y))

			if y < l2 and s2[y] == s3[x + y] and (x, y + 1) not in visited:
				q += [(x, y + 1)]
				visited.add((x, y + 1))

		return False