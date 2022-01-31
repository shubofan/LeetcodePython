# time: O(n)
# space: O(k)
import collections


class Solution:
	def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
		n = len(nums)
		sums = [0] * n  # local max sum until i

		q = collections.deque()
		res = nums[0]

		for i in range(n):
			sums[i] = nums[i]

			while q and i - q[0] > k:  # pop all invalid elements
				q.popleft()

			if q:
				sums[i] += sums[q[0]]  # sums[q[[0]]] the largests sum

			res = max(res, sums[i])

			while q and sums[q[-1]] <= sums[i]:  # make q mono decreasing
				q.pop()

			if sums[i] > 0:  # only add element when it is positive.
				q += [i]

		return res
