class Solution:
	# Time O(N*log(Max(P))
	# Space O(1)
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		def get_total_time(piles, speed):  # O(n)
			hours = 0
			for pile in piles:
				hours += (math.ceil(pile / speed))
			return hours

		l, r = 1, max(piles)
		n = len(piles)

		# log(max(p))
		while l < r:
			speed = (l + r) // 2
			hours = get_total_time(piles, speed)
			if hours > h:  # each too slow
				l = speed + 1
			else:
				r = speed
		return l