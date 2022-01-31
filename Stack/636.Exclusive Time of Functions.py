class Solution:
	def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
		res = [0] * n
		stack = []
		for log in logs:
			lst = log.split(':')
			function_id, op, time = int(lst[0]), lst[1], int(lst[2])
			if op == 'start':
				stack += [(function_id, time)]
			else:
				last_time = stack.pop()[1]
				res[function_id] += (time - last_time + 1)
				if stack:
					res[stack[-1][0]] -= (time - last_time + 1)

		return res