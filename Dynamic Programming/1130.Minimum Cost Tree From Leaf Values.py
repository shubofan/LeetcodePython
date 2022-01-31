# for k from i to j
#  res(i, j) = min(res(i, k) + res(k + 1, j) + max(arr[i]...arr[k]) * max(arr[k + 1]...arr[j]))

# with memorization - --> O(n ^ 3)


class Solution:
	def mctFromLeafValues(self, arr: List[int]) -> int:
		return self.helper(arr, 0, len(arr) - 1, {})

	# cache[(l, r)] means the minimum non-leaf nodes sum with leaf nodes from arr[i] to arr[j]):
	def helper(self, arr, l, r, cache):
		if (l, r) in cache:
			return cache[(l, r)]
		if l >= r:
			return 0

		res = float('inf')
		for i in range(l, r):
			rootVal = max(arr[l:i + 1]) * max(arr[i + 1:r + 1])
			res = min(res, rootVal + self.helper(arr, l, i, cache) + self.helper(arr, i + 1, r, cache))

		cache[(l, r)] = res
		return res