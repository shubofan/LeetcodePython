import collections


class Solution:
	"""
	@param s: a string
	@param k: an integer
	@return: a string such that the same characters are at least distance k from each other
	"""

	def rearrangeString(self, s, k):
		dic = collections.Counter(s)
		sorted_cnts = sorted(dic.items(), key=lambda x: dic[x[0]], reverse=True)
		max_cnt = sorted_cnts[0][1]


		# s = aaabbbc -> max_cnt = 3, so create 3 blocks
		# block0 [a,b,c]
		# block1 = [a,b,c]
		# block2 = [a, b]
		blocks = [[] for _ in range(max_cnt)]
		i = 0
		for cnt in sorted_cnts:
			word, fre = cnt[0], cnt[1]
			# fill each word block by block
			for _ in range(fre):
				blocks[i].append(word)
				i = (i + 1) % len(blocks)

		# No need to check the last block
		for i in range(max_cnt - 1):
			if len(blocks[i]) < k:
				return ""

		res = []
		for block in blocks:
			res.extend(block)
		return ''.join(res)
