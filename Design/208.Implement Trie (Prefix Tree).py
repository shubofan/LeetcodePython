class Node:
	def __init__(self):
		self.children = [None] * 26
		self.isEnd = False


class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = Node()

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		cur = self.root

		for w in word:
			if not cur.children[ord(w) - 97]:
				cur.children[ord(w) - 97] = Node()
			cur = cur.children[ord(w) - 97]
		cur.isEnd = True

	def search(self, word: str) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		cur = self.root
		for w in word:
			if not cur.children[ord(w) - 97]:
				return False
			cur = cur.children[ord(w) - 97]
		return cur.isEnd

	def startsWith(self, prefix: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		cur = self.root
		for w in prefix:
			if not cur.children[ord(w) - 97]:
				return False
			cur = cur.children[ord(w) - 97]
		return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)