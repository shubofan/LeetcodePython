import unittest
from collections import defaultdict
from typing import List

class Parser:

	def parse_accept_language(self, header: str, s: set) -> List[str]:
		languages = header.split(', ')
		return list(filter(lambda l: l in s, languages))

	def parse_accept_language2(self, header: str, s: set) -> List[str]:
		supported_language_country = defaultdict(list) # <fr: [fr-FR, fr-CA]>

		for language_country in s:
			country = language_country.split('-')[0]
			supported_language_country[country] += [language_country]

		country_language_lst = header.split(', ')
		res = []

		for pair in country_language_lst:
			# 'en-US'
			if '-' in pair and pair in s and pair not in res:
				res.append(pair)
			# 'en'
			elif '-' not in pair and pair in supported_language_country:
				for language in supported_language_country[pair]:
					if language not in res:
						res.append(language)
		return res


	def parse_accept_language3(self, header: str, s: List[str]) -> List[str]:
		supported_language_country = defaultdict(list)

		for language_country in s:
			country = language_country.split('-')[0]
			supported_language_country[country] += [language_country]

		country_language_lst = header.split(', ')

		res = []
		for pair in country_language_lst:
			# 'en-US'
			if '-' in pair and pair in s and pair not in res:
				res.append(pair)
			# 'en'
			elif '-' not in pair and '*' not in pair and pair in supported_language_country:
				for language in supported_language_country[pair]:
					if language not in res:
						res.append(language)
			elif '*' in header:

				for language in list(s):
					if language not in res:
						res.append(language)
				break
		return res

	def parse_accept_language4(self, header: str, s: List[str]) -> List[str]:
		res = []
		weighted_header = header.split(',')
		language_tuples = []

		for h in weighted_header:
			split = h.split(';q=')
			weight = split[1]
			language_tuples += [(float(weight), split[0])]

		language_tuples.sort(reverse=True)

		# Check duplicate
		dup = set()

		supported_language_country = defaultdict(list)

		# {fr: [fr-CA, fr-BG]}
		for language_country in s:
			language = language_country.split('-')[0]
			supported_language_country[language] += [language_country]

		is_asterisk_present = False
		asterisk_score = 0

		for t in language_tuples:
			score = t[0]
			candidate = t[1]

			# en-US
			if '-' in candidate and candidate not in dup:
				res += [(score, candidate)]
				dup.add(candidate)
			# fr
			elif '-' not in candidate and candidate != '*':
				for language in supported_language_country[candidate]:
					if language not in dup:
						res.append((score, language))
						dup.add(language)
			#  *
			elif '*' == candidate:
				is_asterisk_present = True
				asterisk_score = score

		# (asterisk_score, other_word)
		if is_asterisk_present:
			for other in s:
				if other not in dup:
					res += [(asterisk_score, other)]

		# [(1.0, 'fr-FR'), (0.8, 'fr-CA'), (0.5, 'en-US'), (0.1, 'fr-BG')]
		res.sort(reverse=True)

		return [t[1] for t in res]


class TestClass(unittest.TestCase):

	def __init__(self, *args, **kwargs):
		super(TestClass, self).__init__(*args, **kwargs)
		self.p = Parser()

	def test_parse_accept_language(self):
		self.assertEqual(self.p.parse_accept_language('en-US, fr-CA, fr-FR', set(['fr-FR', 'en-US'])), ['en-US', 'fr-FR'])
		self.assertEqual(self.p.parse_accept_language('fr-CA, fr-FR', set(['en-US', 'fr-FR'])), ['fr-FR'])

	def test_parse_accept_language2(self):
		self.assertEqual(self.p.parse_accept_language2('en-US, fr-CA, fr-FR', set(['fr-FR', 'en-US'])), ['en-US', 'fr-FR'])
		self.assertEqual(self.p.parse_accept_language2('fr-CA, fr-FR', set(['en-US', 'fr-FR'])), ['fr-FR'])
		self.assertEqual(self.p.parse_accept_language2('en', set(["en-US", "fr-CA", "fr-FR"])), ['en-US'])
		self.assertEqual(self.p.parse_accept_language2('fr', set(["en-US", "fr-CA", "fr-FR"])), ['fr-CA', 'fr-FR']) # How to deal with order ?
		self.assertEqual(self.p.parse_accept_language2('fr-FR, fr', set(["en-US", "fr-CA", "fr-FR"])), ['fr-FR', 'fr-CA'])

	def test_parse_accept_language2(self):
		self.assertEqual(self.p.parse_accept_language3('en-US, fr-CA, fr-FR', set(['fr-FR', 'en-US'])), ['en-US', 'fr-FR'])
		self.assertEqual(self.p.parse_accept_language3('fr-CA, fr-FR', set(['en-US', 'fr-FR'])), ['fr-FR'])
		self.assertEqual(self.p.parse_accept_language3('en', set(["en-US", "fr-CA", "fr-FR"])), ['en-US'])
		# self.assertEqual(self.p.parse_accept_language3('fr', set(["en-US", "fr-CA", "fr-FR"])), ['fr-CA', 'fr-FR']) # How to deal with order ?
		# self.assertEqual(self.p.parse_accept_language3('fr-FR, fr', set(["en-US", "fr-CA", "fr-FR"])), ['fr-FR', 'fr-CA'])

		self.assertEqual(self.p.parse_accept_language3('fr-FR, *', ["en-US", "fr-CA", "fr-FR"]), ['fr-FR', 'en-US', 'fr-CA']) # is that possible that asterisk will be given at first or in the middle ? if so, how the order will be look like
		self.assertEqual(self.p.parse_accept_language3('en-US, *', ["en-US", "fr-CA", "fr-FR"]), ['en-US', 'fr-CA', 'fr-FR'])

	# def test_parse_accept_language2(self):
	#     self.p = Parser()
	#     self.assertEqual(self.p.parse_accept_language2('en-US,fr-CA,fr-FR', set(['fr-FR', 'en-US'])), ['en-US', 'fr-FR'])
	#     self.assertEqual(self.p.parse_accept_language2('fr-CA,fr-FR', set(['en-US', 'fr-FR'])), ['fr-FR'])
	#     self.assertEqual(self.p.parse_accept_language2('en', ["en-US", "fr-CA", "fr-FR"]), ['en-US'])
	#     self.assertEqual(self.p.parse_accept_language2('fr', ["en-US", "fr-CA", "fr-FR"]), ['fr-CA', 'fr-FR']) # How to deal with order ?
	#     self.assertEqual(self.p.parse_accept_language2('fr-FR,fr', ["en-US", "fr-CA", "fr-FR"]), ['fr-FR', 'fr-CA'])
	#     self.assertEqual(self.p.parse_accept_language2('fr-FR,*', ["en-US", "fr-CA", "fr-FR"]), ['fr-FR', 'en-US', 'fr-CA']) # is that possible that asterisk will be given at first or in the middle ? if so, how the order will be look like
	#     self.assertEqual(self.p.parse_accept_language2('en-US,*', ["en-US", "fr-CA", "fr-FR"]), ['en-US', 'fr-CA', 'fr-FR'])
	#     self.assertEqual(self.p.parse_accept_language3('fr-FR;q=1,fr-CA;q=0,*;q=0.5', ["fr-FR", "fr-CA", "fr-BG", 'en-US']), ['fr-FR', 'fr-BG', 'en-US', 'fr-CA'])
	#     self.assertEqual(self.p.parse_accept_language3('fr-FR;q=1,fr-CA;q=0.8,*;q=0.5,fr;q=0.1', ["fr-FR", "fr-CA", "fr-BG", 'en-US']),
	#                      ['fr-FR', 'fr-CA', 'en-US', 'fr-BG'])


if __name__ == '__main__':
	unittest.main()