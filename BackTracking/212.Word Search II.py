from typing import List

# Why Trie

# Intuitively, start from every cell and try to build a word in the dictionary.
# Backtracking (dfs) is the powerful way to exhaust every possible ways.
# Apparently, we need to do pruning when current character is not in any word.
class Solution:
	# O(M*(4^(3L−1)))
	# M是二维网格中的单元格数，L是单词的最大长度。
	#
	# 计算回溯算法将执行的确切步数是一个棘手的问题。我们为这个问题的最坏情况提供了该步骤的上限。该算法循环遍历二维网格中的所有单元，因此在复杂度公式中我们有
	# M作为因子。然后将其归结为每个启动单元所需的最大步骤数（即 4⋅3^(L-1))

	# 假设单词的最大长度是L，从一个单元格开始，最初我们最多可以探索
	# 4个方向。假设每个方向都是有效的（即最坏情况），在接下来的探索中，我们最多有
	# 3个相邻的单元（不包括我们来的单元）要探索。因此，在回溯探索期间，我们最多遍历
	# 4⋅3^(L-1)个单元格。

	# 你可能会想最坏的情况是什么样子。这里有一个例子。想象一下，二维网格中的每个单元都包含字母
	# a，单词词典包含一个单词['aaaa']。这是算法将遇到的最坏的情况之一。

	# Trie {'o': {'a': {'t': {'h': {'$': 'oath'}}}},
	# 'p': {'e': {'a': {'$': 'pea'}}}, 'e': {'a': {'t': {'$': 'eat'}}}, 'r': {'a': {'i': {'n': {'$': 'rain'}}}}}
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		WORD_KEY = '$'

		trie = {}
		for word in words:
			node = trie
			for letter in word:
				# retrieve the next node; If not found, create a empty node.
				node = node.setdefault(letter, {})
			# mark the existence of a word in trie node
			node[WORD_KEY] = word

		rowNum = len(board)
		colNum = len(board[0])

		matchedWords = []

		# print(trie)
		def backtracking(row, col, trie):

			letter = board[row][col]
			currNode = trie[letter]

			# check if we find a match of word
			word_match = currNode.pop(WORD_KEY, False)
			if word_match:
				# also we removed the matched word to avoid duplicates,
				#   as well as avoiding using set() for results.
				matchedWords.append(word_match)

			# Before the EXPLORATION, mark the cell as visited
			board[row][col] = '#'

			# Explore the neighbors in 4 directions, i.e. up, right, down, left
			for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
				newRow, newCol = row + rowOffset, col + colOffset
				if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
					continue
				if not board[newRow][newCol] in currNode:
					continue
				backtracking(newRow, newCol, currNode)

			# End of EXPLORATION, we restore the cell
			board[row][col] = letter

			# Optimization: incrementally remove the matched leaf node in Trie.
			if not currNode:
				trie.pop(letter)

		for row in range(rowNum):
			for col in range(colNum):
				# starting from each of the cells
				if board[row][col] in trie:
					backtracking(row, col, trie)

		return matchedWords

	# class Solution:
	# 	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
	# 		res = set()
	# 		m, n = len(board), len(board[0])
	# 		for word in words:
	# 			# print(word, self.search(board, word, set()))
	# 			for x in range(m):
	# 				for y in range(n):
	# 					if board[x][y] == word[0]:
	# 						if self.search(board, word, set(), x, y, 0):
	# 							res.add(word)
	#
	# 		return list(res)
	#
	# 	def search(self, board, word, seen, x, y, idx) -> bool:
	# 		# print(word, idx)
	# 		m, n = len(board), len(board[0])
	# 		if idx == len(word):
	# 			return True
	# 		if (x, y) in seen:
	# 			return False
	# 		if x < 0 or y < 0 or x >= m or y >= n:
	# 			return False
	# 		if board[x][y] != word[idx]:
	# 			return False
	# 		seen.add((x, y))
	# 		found = self.search(board, word, seen, x + 1, y, idx + 1) or self.search(board, word, seen, x - 1, y,
	# 		                                                                         idx + 1) or self.search(board,
	# 		                                                                                                 word, seen,
	# 		                                                                                                 x, y + 1,
	# 		                                                                                                 idx + 1) or self.search(
	# 			board, word, seen, x, y - 1, idx + 1)
	# 		seen.remove((x, y))
	# 		return found
