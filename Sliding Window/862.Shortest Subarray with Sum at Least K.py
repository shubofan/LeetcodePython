import collections


class Solution:
	def shortestSubarray(self, nums: List[int], k: int) -> int:
		q = collections.deque()
		n = len(nums)
		cur_sum = [0] * (n + 1)

		for i in range(n):
			cur_sum[i + 1] = nums[i] + cur_sum[i]

		# cur_sum[i] = sum[:i-1]
		res = n + 1

		for i in range(n + 1):
			while q and cur_sum[q[-1]] >= cur_sum[i]:  # keep monoqueue increase so the cur_sum[r] - cur_sum[l] > 0
				q.pop()
			while q and cur_sum[i] - cur_sum[q[0]] >= k:  # q[0] is l : sum [0, i- 1] - sum[0, l -1] = sum [l, i - 1] -> total length is i-1 - l + 1 = i-l
				res = min(res, i - q.popleft())  # total length is i-1 - l + 1 = i-l, if length is shorter, update
			q += [i]
		return -1 if res == n + 1 else res  # if sum of nums < k: res == n + 1, no solution, return -1
