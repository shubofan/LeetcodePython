class Solution:
	def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
		visited = set()
		q = collections.deque()
		# (water in jug1, water in jug2)
		q += [(0, 0)]

		while q:
			j1, j2 = q.popleft()
			visited.add((j1, j2))
			if j1 + j2 == targetCapacity:
				return True

			moves = set(
				[
					# fill j1
					(jug1Capacity, j2),
					# fill j2
					(j1, jug2Capacity),
					# empty j1
					(0, j2),
					# empty j2
					(j1, 0),
					# pour j2 to j1
					(min(j1 + j2, jug1Capacity), (j1 + j2) - min(j1 + j2, jug1Capacity)),

					# pour j1 to j2
					((j1 + j2) - min(j1 + j2, jug2Capacity), min(j1 + j2, jug2Capacity)),
				])
			q.extend(moves - visited)
		return False