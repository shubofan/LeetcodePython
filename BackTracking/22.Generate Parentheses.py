from typing import List


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		self.res = []

		def helper(l, r, n, path):

			if l == r == n:
				self.res += [path]
				return
			if l < n:
				helper(l + 1, r, n, path + '(')
			if r < l:
				helper(l, r + 1, n, path + ')')

		helper(0, 0, n, '')
		return self.res

if __name__ == '__main__':
    s = Solution()

    print(s.generateParenthesis(2))