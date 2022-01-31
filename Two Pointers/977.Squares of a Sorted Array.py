class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		n = len(nums)
		l, r = 0, n - 1

		# Write res from back to front using pointer idx
		res = [0] * n
		idx = r

		while l <= r:
			if abs(nums[l]) < abs(nums[r]):
				res[idx] = nums[r] ** 2
				r -= 1
			else:
				res[idx] = nums[l] ** 2
				l += 1

			idx -= 1

		return res

class Solution:
	def sortedSquares(self, nums: List[int]) -> List[int]:
		n = len(nums)

		i = 0
		# find pivot
		while i < n:
			if nums[i] < 0:
				i += 1
			else:
				break
		j = i - 1

		res = []

		# from middle to left and right
		while j >= 0 and i < n:
			if nums[j] ** 2 >= nums[i] ** 2:
				res += [nums[i] ** 2]
				i += 1
			else:
				res += [nums[j] ** 2]
				j -= 1

		while i < n:
			res += [nums[i] ** 2]
			i += 1

		while j >= 0:
			res += [nums[j] ** 2]
			j -= 1

		return res