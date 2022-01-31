# At every step along the way, we consider exactly 4 different choices or 4 different recursive paths.
# The base case is when the value of index reaches N i.e. the length of the nums array. Hence, our complexity would be O(4^N).

# the space used up by the recursion stack would also be O(N) since the size of recursion stack is determined by the value of index and it goes from 0 all the way to N.
class Solution:
	def addOperators(self, num: str, target: int) -> List[str]:
		self.res = []

		def helper(num, idx, cur_op, pre_op, path, val, target):
			if idx == len(num):
				# val == target and no operand is added to path
				if val == target and cur_op == 0:
					self.res += [path[1:]]
				return

			cur_op = 10 * cur_op + int(num[idx])

			# Do NO OP recursion when current operand > 0, to avoid  1 + 05 or 1 * 05
			if cur_op > 0:
				helper(num, idx + 1, cur_op, pre_op, path, val, target)

			# Add recursion, cur = 0, pre = cur
			helper(num, idx + 1, 0, cur_op, path + '+' + str(cur_op), val + cur_op, target)

			# Can subtract or multiply only if there are some previous operands
			if path:
				helper(num, idx + 1, 0, -cur_op, path + '-' + str(cur_op), val - cur_op, target)
				helper(num, idx + 1, 0, cur_op * pre_op, path + '*' + str(cur_op), val - pre_op + (cur_op * pre_op),
				       target)

		helper(num, 0, 0, 0, '', 0, target)
		return self.res