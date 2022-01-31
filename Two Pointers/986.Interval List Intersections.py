class Solution:
	def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
		l1, l2 = len(firstList), len(secondList)
		if l1 == 0 or l2 == 0:
			return []
		res = []

		i, j = 0, 0

		while i < l1 and j < l2:
			low = max(firstList[i][0], secondList[j][0])
			high = min(firstList[i][1], secondList[j][1])

			if low <= high:
				res += [[low, high]]
			if firstList[i][1] < secondList[j][1]:
				i += 1
			else:
				j += 1

		return res
