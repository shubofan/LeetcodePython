'''
我们可以将字符串 s 按照 0 和 1 的连续段分组，存在 {counts} 数组中，例如 s=00111011  数组：counts={2,3,1,2}。它们能组成的满足条件的子串数目为 min⁡{u,v} 即一对相邻的数字对答案的贡献。

我们只要遍历所有相邻的数对，求它们的贡献总和，即可得到答案。

'''

class Solution:
	def countBinarySubstrings(self, s: str) -> int:
		last = 0
		cur = 0
		res = 0
		n = len(s)

		while cur < n:
			c = s[cur]
			cnt = 0
			while cur < n and c == s[cur]:
				cur += 1
				cnt += 1

			res += min(last, cnt)
			last = cnt
		return res
