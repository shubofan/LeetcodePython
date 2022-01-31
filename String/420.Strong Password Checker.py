class Solution:
	def strongPasswordChecker(self, password: str) -> int:
		missingTypes = 3
		lower, upper, digit = False, False, False
		for w in password:
			if w.islower() and not lower:
				missingTypes -= 1
				lower = True
			if w.isupper() and not upper:
				missingTypes -= 1
				upper = True
			if w.isdigit() and not digit:
				digit = True
				missingTypes -= 1
		n = len(password)

		repeats = 0
		to_change = 0

		one = 0;  # total deletions for 3n repeated chars. e.g. "aaa" needs 1 deletion to fix
		two = 0;  # total deletions for 3n+1 repeated chars. e.g. "aaaa" needs 2 deletions to fix.

		i = 0

		while i < n:
			j = i
			while j < n and password[i] == password[j]:
				j += 1
			repeats = j - i

			if repeats >= 3:
				to_change += repeats // 3
				if repeats % 3 == 0:
					one += 1
				elif repeats % 3 == 1:
					two += 2
			i = j

		if n > 20:
			to_delete = n - 20
			# use delete to save the operation to change
			to_change -= min(to_delete, one)
			# max(0, to_delete - one) is the reamining delete can be used
			to_change -= min(max(0, to_delete - one), two) // 2
			# max(0, to_delete - one - two) is the reamining delete can be used
			to_change -= max(0, to_delete - one - two) // 3
			return to_delete + max(missingTypes, to_change);

		elif n < 6:
			to_add = 6 - n
			return max(to_add, missingTypes)
		else:
			return max(missingTypes, to_change)

