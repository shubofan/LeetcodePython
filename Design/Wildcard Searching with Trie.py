from typing import Dict, List, Any

WILDCARD = '?'


class Trie:
	def __init__(self) -> None:
		self.children: Dict[str: Trie] = {}
		self.isLeaf: bool = False

	def insert(self, key: str) -> None:
		node = self
		for char in key:
			if char not in node.children:
				node.children[char] = Trie()
			node = node.children[char]
		node.isLeaf = True

	def find(self, key: str) -> List[str]:
		stack = [(self, 0, '')]
		result = []

		while stack:
			curr, count, currWord = stack.pop()

			if count == len(key):
				if curr.isLeaf: result.append(currWord)
				continue

			currChar = key[count]
			if currChar == WILDCARD:
				for childChar, node in curr.children.items():
					stack.append((node, count + 1, currWord + childChar))
				continue

			if currChar in curr.children:
				node = curr.children[currChar]
				stack.append((node, count + 1, currWord + currChar))

		return result


def main():
	trie = Trie()
	trie.insert('apple')
	trie.insert('applx')
	trie.insert('amazon')
	trie.insert('google')

	# assert (trie.find('??') == ['oi'])
	# assert (trie.find('') == [])
	# assert (trie.find('w?rd') == ['ward', 'word'])
	# assert (trie.find('???') == ['boi'])
	# assert (trie.find('?oi') == ['boi'])
	print(trie.find('a??le'))
	print(trie.find('a????'))
	print(trie.find('a'))


if __name__ == '__main__':
	main()