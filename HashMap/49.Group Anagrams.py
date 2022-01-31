# Time Complexity: O(N* K*log(K)), where N is the length of strs , and K is the maximum length of a string in strs
# . The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.

# Space Complexity: O(NK), the total information content stored in res.
import collections
from typing import List


class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		dic = collections.defaultdict(list)

		for s in strs:
			dic[''.join(sorted(s))] += [s] #  sorted('asdcv') -> ['a', 'c', 'd', 's', 'v']
		res = []

		for k, v in dic.items():
			res += [v]
		return res