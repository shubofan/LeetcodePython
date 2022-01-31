class Solution:
	"""
	@param word: a non-empty string
	@param abbr: an abbreviation
	@return: true if string matches with the given abbr or false
	"""

	def validWordAbbreviation(self, word, abbr):
		match = ""
		tem = 0

		for a in abbr:
			if a.isdigit():
				if tem == 0 and a == '0':
					return False
				tem = tem * 10 + int(a)
			else:
				match += tem * '.' + a
				tem = 0

		# a and 1 match
		match += tem * '.'

		if len(match) != len(word):
			return False

		for i in range(len(word)):
			if match[i] == '.':
				continue
			if match[i] != word[i]:
				return False

		return True