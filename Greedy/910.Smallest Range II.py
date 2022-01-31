from typing import List


class Solution:
	#     Intuition:
	#         For each integer A[i],
	#         we may choose either x = -K or x = K.

	#         If we add K to all A[i], the result won't change.

	#         It's the same as:
	#         For each integer A[i], we choose either x = 0 or x = 2 * K.

	#     Explanation:
	#         We sort the A first, and we choose to add x = 0 to all A[i].
	#         Now we have res = A[n - 1] - A[0].
	#         Starting from the smallest of A, we add 2 * K to A[i],
	#         hoping this process will reduce the difference.

	#         Update the new mx = max(mx, A[i] + 2 * K)
	#         Update the new mn = min(A[i + 1], A[0] + 2 * K)
	#         Update the res = min(res, mx - mn)

	#     Time Complexity:
	#         O(NlogN), in both of the worst and the best cases.

	def smallestRangeII(self, nums: List[int], k: int) -> int:
		nums.sort()
		n = len(nums)
		res = nums[n - 1] - nums[0]
		max_ = nums[n - 1]
		min_ = nums[0]

		for i in range(n - 1):
			# get possible max value and and min value until i + 1
			max_ = max(nums[i] + 2 * k, max_)
			min_ = min(nums[i + 1], nums[0] + 2 * k)
			res = min(res, max_ - min_)
		return res