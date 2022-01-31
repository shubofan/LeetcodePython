class Solution:
	def reverseWords(self, s: str) -> str:
		lst = s.strip().split(' ')
		lst = filter(lambda x: x != '', lst)

		return ' '.join(reversed(list(lst)))