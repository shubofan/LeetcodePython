class Solution:
	"""
	@param dict: an array of n distinct non-empty strings
	@return: an array of minimal possible abbreviations for every word
	"""

	def wordsAbbreviation(self, dict):
		# i + 1 is the length if prefix
		def get_abb(word, i):
			if len(word) <= 3:
				return word
			# like -> l2e when i = 0
			candidate = word[:i + 1] + str(len(word) - 2 - i) + word[-1]
			# If the abbreviation doesn't make the word shorter, then keep it as original.
			if len(candidate) >= len(word):
				return word
			return candidate

		n = len(dict)
		cnt = collections.Counter()  # <abbreviation, number of words for this abbreviation>
		res = [''] * n

		for i, word in enumerate(dict):
			abbreviation = get_abb(word, 0)
			cnt[abbreviation] += 1
			res[i] = abbreviation

		round = 1

		while True:
			stop = True
			# print(res,cnt)
			for i, abbreviation in enumerate(res):
				# has conflicts
				if cnt[abbreviation] > 1:
					# get new abbreviation
					new_abbreviation = get_abb(dict[i], round)
					cnt[new_abbreviation] += 1
					res[i] = new_abbreviation
					# need to check again
					stop = False
			# no conflict found, so res is good to return
			if stop:
				break
			round += 1
		return res
