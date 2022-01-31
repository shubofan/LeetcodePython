from typing import List


class Solution:
	#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
	#         res = []
	#         if not s:
	#             return []
	#         wordSet=set(wordDict)
	#         # sample {'dog': [['dog']], 'sanddog': [['sand', 'dog']], 'catsanddog': [['cat', 'sand', 'dog'], ['cats', 'and', 'dog']], 'anddog': [['and', 'dog']]})
	#         self.mem = collections.defaultdict(list)
	#         self.dfs(s, wordSet)

	#         for lst in self.mem[s]:
	#             res += [' '.join(lst)]
	#         return res

	#     def dfs(self, s: str, wordSet: Set[str]) -> List[str]:

	#         if not s:
	#             return [[]]
	#         if s in self.mem:
	#             return self.mem[s]
	#         for i in range(len(s)+1):
	#             if s[:i] in wordSet:
	#                 for subsentence in self.dfs(s[i:], wordSet):
	#                     print(subsentence, s[:i])
	#                     self.mem[s].append([s[:i]] + subsentence) # ["dog"] + [] -> ["dog"]
	#         return self.mem[s]

	# worst case
	# s = "aaa...aaa"
	# wordDict = ["a","aa","aaa", ..., "aaa...aaa"]

	# if i = 3, s = 'aaa' -> ('', 'aaa'),(a, aa), ('aa', 'a'),('aaa', '') 4 solutions

	# Time:  O(2^N * N) + O(W)
	# In the above worst case, each postfix of length i would have 2^(i−1) number of
	# solutions, i.e. each edge brings back 2^(i−1) number of solution from the target postfix. Therefore, in total,
	# we need (∑Ni=12i−1)=(2^N) iterations to construct the final solutions. Function will be called 2^N times,
	# each function call will take O(N) for writing(self.res += [' '.join(path)]). So total O(2^N * N) + O(W)

	# Space: there are total (2^N) ways to split s and each split take O(N) to store. So total  O(2^N * N)
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

		if not s:
			return []
		# O(W), w is the size of wordDict
		self.wordSet = set(wordDict)
		self.res = []
		self.dfs(s, [])
		return self.res

	def dfs(self, s: str, path: List[str]) -> None:
		# The s can be successfully break down.
		if not s:
			self.res += [' '.join(path)]
			return
		# O(2^N * N)
		for i in range(len(s) + 1):
			word = s[:i]
			if word in self.wordSet:
				self.dfs(s[i:], path + [word])