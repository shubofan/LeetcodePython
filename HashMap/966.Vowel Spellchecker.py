from typing import List


class Solution:
	def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

		res = []

		wordset = set()

		cap = {}
		vowel = {}

		for word in wordlist:
			wordset.add(word)
			if word.lower() not in cap:
				cap[word.lower()] = word

			key = ''.join(['*' if c in 'aeiou' else c
			               for c in word.lower()])
			if key not in vowel:
				vowel[key] = word

		for query in queries:
			if query in wordset:
				res += [query]
			elif query.lower() in cap:
				res += [cap[query.lower()]]
			elif ''.join(['*' if c in 'aeiou' else c
			              for c in query.lower()]) in vowel:

				res.append(vowel[
					           ''.join(['*' if c in 'aeiou' else c for c in query.lower()])
				           ]
				           )

			else:
				res += ['']

		return res