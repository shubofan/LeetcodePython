# Problem 1: Special Constraint
	#
	# The integers in arr are distinct.
	# The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
	# sum(pieces[i].length) == arr.length.
from typing import List


class Solution:
	def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
		map = {}
		for p in pieces:
			map[p[0]] = p

		n = len(arr)
		i = 0
		while i < n:
			if arr[i] not in map:
				return False
			p = map[arr[i]]
			if arr[i:i + len(p)] != p:
				return False
			i += len(p)
		return True

# Complexity
#
#     Time: O(N), where N is number of elements in array arr.
#     Space: O(N)
#
# Problem 2: Follow up question
#
#     The integers in arr can be duplicated.
#     The integers in pieces can be duplicated.
#     sum(pieces[i].length) != arr.length.
#
# Example 1:
# Input: arr = [4,91,4,64,78], pieces = [[78],[4],[4,64],[91]]
# Output: true
#
# Example 2:
# Input: arr = [4,91,4,64,78], pieces = [[78],[4],[4,64],[91], [5]]
# Output: false

class Solution:
	def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
		pieces.sort(key=lambda x: -len(x))  # Sort by decreasing order of length of pieces to avoid
		# case an bigger array contains another array, but bigger array is processed later

		m = sum(len(p) for p in pieces)
		seen = set()

		n = len(arr)
		i = 0
		while i < n:
			good = False
			for j, p in enumerate(pieces):
				if j in seen: continue
				if arr[i:i + len(p)] == p:
					good = True
					i += len(p)
					seen.add(j)
					break
			if not good: return False
		return i == m

# Complexity:
#
#     Time: O(NlogN + N*M), where N is number of elements in array arr, M is number of elements in pieces after flat into 1D.
#     Space: O(M)
