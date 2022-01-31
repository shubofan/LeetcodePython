class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		if not p:
			return not s
		# p like: a*
		if len(p) > 1 and p[1] == '*':
			# a* -> "", match 0 time,          #s[0] match p[0], try to match s[1:] and same p because a* can use multiple times
			return self.isMatch(s, p[2:]) or (s and (s[0] == p[0] or p[0] == '.')) and self.isMatch(s[1:], p)
		# p like aa or .a
		else:
			return s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])