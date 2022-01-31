from typing import List


class Solution:
	def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
		slots1.sort(key=lambda slot: (slot[0], slot[1]))
		slots2.sort(key=lambda slot: (slot[0], slot[1]))

		i, j = 0 ,0

		while i < len(slots1) and j < len(slots2):
			if slots1[i][1] <= slots2[j][0]:
				i += 1
			elif slots1[i][1] > slots2[j][0]:
				j += 1

			else: # find a overlap
				start = max(slots1[i][0], slots2[j][0])
				end = min(slots1[i][1], slots2[j][1])

				if end - start >= duration:
					return [start, start + duration]
				else:
					if slots1[i][1] > slots2[j][1]:
						j += 1
					else:
						i += 1
		return []