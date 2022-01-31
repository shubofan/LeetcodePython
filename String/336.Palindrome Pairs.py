from typing import List


class Solution:
	# O(N * K^2) N is the size of words, K is the max length of word.
	def palindromePairs(self, words: List[str]) -> List[List[int]]:
		dic = {}
		res = []

		# <word, idx of word in lst>
		# O(N)
		for idx, word in enumerate(words):
			dic[word] = idx

		# O(N * K^2) N is the size of words, K is the max length of word.
		for idx, word in enumerate(words):
			# split each word to find if it can concatenate with other words to form a palindrome
			if word:

				# word itself is a palindrome
				if '' in dic and word == word[::-1]:
					res += [[dic[''], idx]]  # add (dic[''], odx)

				# if i = 0, r is word,l[::-1] is '', add (idx, dic[''])
				for i in range(len(word)):  # O(K^2)
					l = word[:i]
					r = word[i:]

					# l is palindrome, r[::-1] in the words list, new palindrome (r[::-1]-l-r)
					if l == l[::-1] and r[::-1] in dic and dic[r[::-1]] != idx:  # Check if l is palindrome take up to O(K)
						res += [[dic[r[::-1]], idx]]
					# r is palindrome, l[::-1] in the words list, new palindrome (l-r-l[::-1])
					if r == r[::-1] and l[::-1] in dic and dic[l[::-1]] != idx:  # avoid add [0, 0] for ["a",""]
						res += [[idx, dic[l[::-1]]]]

		return res

