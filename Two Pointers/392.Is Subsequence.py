# 时间复杂度：O(n+m)，每次无论是匹配成功还是失败，都有至少一个指针发生右移，两指针能够位移的总距离为 m + n
#
# 空间复杂度：O(1)

from bisect import bisect_left
from collections import defaultdict

#     def isSubsequence(self, s: str, t: str) -> bool:
#         if not s:
#             return True
#         if len(s) > len(t):
#             return False

#         i, j = 0, 0

#         while j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             if i == len(s):
#                 return True
#             j += 1
#         return False

# follow up

# pre-process T

# complexity of one search for string S_i is O(m_i)*log(n), where m_i is length of string and we have log(n) factor, because we potentially can have list of indexes with length n.
# So if m is the longest length of S_i,
# we have complexity O(k m log n), when two-pointer approach has O(k n) complexity. So, if length of original string n is big and m is small -> (m<<n), it is worth to use this method.
'''
    // Eg-1. s="abc", t="bahbgdca"
    // idx=[a={1,7}, b={0,3}, c={6}]
    //  i=0 ('a'): prev=1
    //  i=1 ('b'): prev=3
    //  i=2 ('c'): prev=6 (return true)

    // Eg-2. s="abc", t="bahgdcb"
    // idx=[a={1}, b={0,6}, c={5}]
    //  i=0 ('a'): prev=1
    //  i=1 ('b'): prev=6
    //  i=2 ('c'): prev=? (return false)

'''


class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		mapIndices = defaultdict(list)
		for i, c in enumerate(t):
			mapIndices[c].append(i)

		prev = 0  # previous index in t
		for i, c in enumerate(s):
			j = bisect_left(mapIndices[c], prev)
			# print(i ,c , prev, j, mapIndices[c])
			if j == len(mapIndices[c]): return False
			prev = mapIndices[c][j] + 1
		return True
