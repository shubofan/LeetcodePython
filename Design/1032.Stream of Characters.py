# Construct Trie with Reversed Words

# Time complexity: O(WQ)

# W = max(words.length),the maximum length of all words.
# N = words.size, the number of words
# Q, the number of calls of function query

class Node:
	def __init__(self):
		self.isWord = False
		self.children = {}


class StreamChecker:

	def __init__(self, words: List[str]):
		self.sb = ''
		self.root = Node()
		for word in words:
			cur = self.root
			for c in word[::-1]:
				if c not in cur.children:
					cur.children[c] = Node()
				cur = cur.children[c]
			cur.isWord = True

	# print(self.root.children)

	def query(self, letter: str) -> bool:
		self.sb += letter
		i = len(self.sb) - 1
		cur = self.root

		while i >= 0:
			if cur.isWord:
				return True
			if self.sb[i] not in cur.children:
				return False
			cur = cur.children[self.sb[i]]
			i -= 1
		return cur.isWord

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)222