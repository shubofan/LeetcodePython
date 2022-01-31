class Solution:

	# Let's use three pointers two, three and five to mark the last ugly number which was multiplied by 2, 3 and 5, correspondingly.

	# choose the smallest ugly number among 2 × nums[two]， 3 × nums[three], and 5 × nums[five] and add it into the array. Move the corresponding pointer by one step.

	def nthUglyNumber(self, n: int) -> int:
		res = [1]
		two = 0
		three = 0
		five = 0

		while len(res) < n:
			min_ = min(res[two] * 2, res[three] * 3, res[five] * 5)
			if res[two] * 2 == min_:
				two += 1

			if res[three] * 3 == min_:
				three += 1

			if res[five] * 5 == min_:
				five += 1

			res += [min_]

		return res[-1]