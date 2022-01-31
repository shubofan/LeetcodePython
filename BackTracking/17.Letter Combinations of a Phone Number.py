


'''
Time complexity : O(3^N × 4^M)

where N is the number of digits in the input that maps to 3 letters ( e.g. 2, 3, 4, 5, 6, 8 )
and M is the number of digits in the input that maps to 4 letters ( e.g. 7, 9 ) and N+M is the total number digits in the input.

Space complexity : O(3^N×4^M) since one has to keep3^N×4^M solutions.

'''

from typing import List


class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		self.dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
		            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
		self.res = []
		lst = list(digits)
		if not lst:
			return []
		self.helper(lst, 0, [])
		return self.res

	def helper(self, digits: List[str], idx: int, path: str) -> None:
		if len(path) == len(digits):
			self.res += [''.join(path)]
			return
		else:
			for c in self.dic[digits[idx]]:
				self.helper(digits, idx + 1, path + [c])
