class Solution:

	# Time: O(N * 26 * W^2 + A), where N <= 1000 is number of words in wordList, W <= 5 is length of each words, A is total number of sequences.
	#     BFS costs O(E + V), where E is number of edges, V is number of vertices.
	#     Because words need to be existed in the wordList, so there is total N words, it's also the number of vertices.
	#     To find neighbors for a word, it costs O(26 * W * W), in the worst case, we have to find the neighbors of N words, so there is total O(N * 26 * W^2) edges.

	# Space: O(N*W + A)

	def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
		words = set(wordList)
		if endWord not in words: return []
		dic = collections.defaultdict(list)  # '*og': ['log', 'cog', 'dog']
		n = len(wordList[0])
		for w in words:
			for i in range(n):
				dic[w[:i] + '*' + w[i + 1:]].append(w)

		# two queues + level order bfs
		q, next_q = [(beginWord, [beginWord])], []
		res = []
		seen = set()
		while q:
			while q:
				w, path = q.pop()
				seen.add(w)
				if w == endWord: res.append(path)
				for i in range(n):
					for nxt in dic[w[:i] + '*' + w[i + 1:]]:
						if nxt not in seen:
							next_q.append((nxt, path + [nxt]))
			if res: return res

			q, next_q = next_q, []
		return []
