from collections import deque


class Node:
	def __init__(self, word: str):
		self.word = word
		self.lst = []
		self.lv = 1


class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		root = Node(beginWord)
		root.lst += [beginWord]
		q = deque()
		q.append(root)
		s = "abcdefghijklmnopqrstuvwxyz"
		if endWord not in wordList:
			return 0
		wordListSet = set(wordList)

		while q:
			size = len(q)
			added = set()
			for i in range(size):
				node = q.popleft()
				word, lst, lv = node.word, node.lst, node.lv
				lstset = set(lst)
				if word == endWord:
					return lv

			for i in range(len(word)):
				tem = list(word)
				for replacement in s:
					tem[i] = replacement
					newStr = ''.join(tem)
					if newStr in wordListSet and newStr not in lstset and newStr not in added:
							# print(newStr, i)
						added.add(newStr)
						node = Node(newStr)
						node.lst = lst[::]
						node.lst += [newStr]
						node.lv = lv + 1
						q.append(node)
		return 0
