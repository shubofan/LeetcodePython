class Solution:
	def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
		lst = []

		for t in trips:
			n, fro, to = t[0], t[1], t[2]

			lst += [[fro, n]]
			lst += [[to, -n]]

		lst.sort()  # sort by location
		for pair in lst:
			capacity -= pair[1]
			if capacity < 0:
				return False

		return True