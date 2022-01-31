import random


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
	def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

		def match(w1, w2):
			cnt = 0
			for i in range(len(w1)):
				if w1[i] == w2[i]:
					cnt += 1
			return cnt

		while True:
			random_idx = random.randrange(len(wordlist))
			word = wordlist[random_idx]
			numOfMatched = master.guess(word)
			if numOfMatched == 6:
				return

			new_wordlist = []
			for w in wordlist:
				if match(word, w) == numOfMatched:
					new_wordlist += [w]
			wordlist = new_wordlist