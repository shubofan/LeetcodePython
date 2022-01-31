class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		dic = {} #<letter, idx>
		for idx, letter in enumerate(order):
			dic[letter] = idx

		for idx, word in enumerate(words):
			if idx == 0:
				continue
			pre_word = words[idx - 1]
			i = 0
			l1, l2 = len(pre_word), len(word)
			while i < l1 and i < l2:
				if dic[pre_word[i]] < dic[word[i]]:
					break
				elif dic[pre_word[i]] > dic[word[i]]:
					return False
				else:
					i += 1
			#  l1:aa, l2:a      -> false
			if l1 != l2 and i == l2:
				return False
		return True