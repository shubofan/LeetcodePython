class Solution:

	##T : O(A ^ N) [A = 10 , N = 4] --> We Only Visit all Possible nodes once(by using HashSet) and will not visit deadends
	#                                --> Because (Max(Possible + deadends) = A ^ N), it's time complexity is O(A^N)

	##S : O(A ^ N) [A = 10 , N = 4] --> Same As Time Complexity (Max(HashSet(Visited) + HashSet(deadends) = A^N)
	def openLock(self, deadends: List[str], target: str) -> int:
		q = collections.deque()
		seen = set(deadends)

		if '0000' in seen:
			return -1

		q += [('0000', 0)]

		while q:
			code, step = q.popleft()

			if code == target:
				return step

			for i in range(4):
				digit = int(code[i])

				digit_plus = '0' if digit == 9 else str(digit + 1)
				digit_minus = '9' if digit == 0 else str(digit - 1)

				next_plus = code[:i] + digit_plus + code[i + 1:]
				next_minus = code[:i] + digit_minus + code[i + 1:]

				if next_plus not in seen:
					q += [(next_plus, step + 1)]
					seen.add(next_plus)

				if next_minus not in seen:
					q += [(next_minus, step + 1)]
					seen.add(next_minus)

		return -1