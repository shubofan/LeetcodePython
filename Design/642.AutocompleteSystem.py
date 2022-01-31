import collections
import heapq


class TrieNode:
	def __init__(self):
		self.isEnd = False
		self.children = {}
		self.fre = collections.defaultdict(int) # <sentence(prefix), frequency>

class sentenceWithFre:
	def __init__(self, sentence, frequency):
		self.sentence = sentence
		self.frequency = frequency
	def __lt__(self, other):
		if self.frequency == other.frequency:
			# same fre, larger ASCII will be treat as smaller -> larger ASCII will be popped at first
			return self.sentence > other.sentence
		return self.frequency < other.frequency

class AutocompleteSystem:
	def __init__(self, sentences, times):
		self.root = TrieNode()
		# record all the input got so far
		self.str = ''
		# cur node in the Trie
		self.cur = self.root
		for i in range(len(sentences)):
			self.__insert__(sentences[i], times[i])

	def input(self, c):
		res = []
		if c == '#': # save sentence and reset state
			self.__insert__(self.str, 1)
			self.str = ''
			self.cur = self.root
			return res
		self.str += c
		if c not in self.cur.children:
			self.cur.children[c] = TrieNode()
		self.cur = self.cur.children[c]
		return self.__getTop3__(self.cur, res)

	def __getTop3__(self, node, res):
		if not node:
			return res
		pq = []
		for sentence, fre in node.fre.items():
			heapq.heappush(pq, sentenceWithFre(sentence, fre))
			if len(pq) == 4:
				heapq.heappop(pq)

		while pq:
			res += [heapq.heappop(pq).sentence]
		return res[::-1]

	# insert a sentence with its time to Tries
	def __insert__(self, sentence, time):
		node = self.root
		for c in sentence:
			if c not in node.children:
				node.children[c] = TrieNode()
			node = node.children[c]
			node.fre[sentence] += time
		node.isEnd = True

if __name__ == '__main__':
	auto = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])


	# Operation: input('i')
	# Output: ["i love you", "island","i love leetcode"]
	# Explanation:
	# There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree.
	# Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman".
	# Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

	# Operation: input(' ')
	# Output: ["i love you","i love leetcode"]
	# Explanation:
	# There are only two sentences that have prefix "i ".
	# Operation: input('a')
	# Output: []
	# Explanation:
	# There are no sentences that have prefix "i a".
	# Operation: input('#')
	# Output: []
	# Explanation:
	# The user finished the input, the sentence "i a" should be saved as a historical sentence in system.
	# And the following input will be counted as a new search.

	print(auto.input('i'))
	print(auto.input(' '))

	print(auto.input('#'))

	# return ["i love you","i love leetcode"] again, since restart search
	print(auto.input('i'))


