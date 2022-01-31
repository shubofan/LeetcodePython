class Solution:
	def toGoatLatin(self, sentence: str) -> str:
		lst = sentence.split(' ')
		for idx, s in enumerate(lst):
			tem = ''
			if s[0] not in 'aeiouAEIOU':
				tem += s[1:] + s[0]
			else:
				tem = s
			tem += 'ma' + 'a' * (idx + 1)
			lst[idx] = tem

		return ' '.join(lst)