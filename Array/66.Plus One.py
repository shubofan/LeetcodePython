class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		i = len(digits) - 1
		# move from end to start
		while i >= 0:
			# if meet 9, set current to 0
			if digits[i] == 9:
				digits[i] = 0
				i -= 1
			else:
				# return plus 1
				digits[i] += 1
				return digits
		# like [9,9,9] -> 1 + [0,0,0] = [1,0,0,0]
		return [1] + digits
