import collections


class Solution:
	def lengthLongestPath(self, input: str) -> int:
		path = input.split('\n')
		d = collections.defaultdict(int) # <depth, length of file/folder in this depth>
		res = 0

		for folder in path:
			depth = folder.count('\t')
			d[depth] = d[depth - 1] + len(folder) - depth  # depth is the number of \t -> size of \t is 1

			if '.' in folder:
				res = max(res, d[depth] + depth)  # depth == number of slashs(/) , so need to add it

		return res