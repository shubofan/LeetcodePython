from typing import List


class Solution:
	# Time Complexity: O(NQ), where N is the length of S , and we have Q replacement operations.
	# Space Complexity: O(N), if we consider targets[i].length <= 100 as a constant bound.
	def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
		dic = {}  # <start_index_to_index, idx in indices/sources/targets>
		res = []

		k = len(indices)

		for i in range(k):
			start = indices[i]
			length = len(sources[i])
			if s[start:start + length] == sources[i]:
				dic[start] = i

		i = 0
		while i < len(s):
			if i in dic:  # replace s[i:i+lenth] with targets[idx]
				idx = dic[i]
				length = len(sources[idx])
				res += [targets[idx]]
				i += length
			else:
				res += s[i]
				i += 1

		return ''.join(res)

	# Time Complexity: O(NQ), where N is the length of S , and we have Q replacement operations.
	# Space Complexity: O(N), if we consider targets[i].length <= 100 as a constant bound.
	def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
		# sort by indices decreasingly
		# Then replace start from right, so we don't need to calculate the length
		for i, source, t in sorted(zip(indices, sources, targets), reverse=True):
			if s[i:i + len(source)] == source:
				s = s[:i] + t + s[i + len(source):]
		return s