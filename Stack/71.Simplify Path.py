class Solution:
	def simplifyPath(self, path: str) -> str:
		if not path:
			return ''

		dirs = path.split('/')
		stack = []

		for d in dirs:
			if d == '..':
				if stack:
					stack.pop()
			elif d == '.':
				continue
			elif d:  # d is not empty string
				stack += [d]

		res = '/'
		while stack:
			res += stack.pop(0) + '/'

		return res if res == '/' else res[:len(res) - 1]  # when path is "/../", stack = [], res = '/', so we don't remove last '/'