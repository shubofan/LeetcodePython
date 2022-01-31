import collections


class TrieNode:
	def __init__(self):
		self.children = collections.defaultdict(TrieNode)
		self.isEnd = False


class WordDictionary:

	def __init__(self):
		self.root = TrieNode()

	def addWord(self, word: str) -> None:
		cur = self.root
		for w in word:
			cur = cur.children[w]
		cur.isEnd = True

	def search(self, word: str) -> bool:

		return self.find(word, self.root)

	def find(self, word: str, cur: TrieNode) -> None:
		for i in range(len(word)):
			if word[i] == '.':
				for child in cur.children.values():
					if self.find(word[i + 1:], child):
						return True
				return False
			else:
				if word[i] not in cur.children:
					return False
			cur = cur.children[word[i]]

		return cur.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)