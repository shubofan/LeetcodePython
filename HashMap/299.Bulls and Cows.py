import collections


class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		a, b = 0, 0
		cnt = collections.Counter(secret)
		for i, c in enumerate(guess):
			if c in cnt:
				if c == secret[i]:
					a += 1
					if cnt[c] <= 0:
						b -= 1
				else:
					if cnt[c] > 0:
						b += 1
				cnt[c] -= 1

		return str(a) + 'A' + str(b) + 'B'


class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		a, b = 0, 0
		cnt = collections.Counter(secret)
		for i, c in enumerate(guess):
			if c == secret[i]:
				a += 1
				cnt[c] -= 1
				if cnt[c] == 0:
					cnt.pop(c)

		for i, c in enumerate(guess):
			if c in cnt and c != secret[i]:
				b += 1
				cnt[c] -= 1
				if cnt[c] == 0:
					cnt.pop(c)
		return str(a) + 'A' + str(b) + 'B'