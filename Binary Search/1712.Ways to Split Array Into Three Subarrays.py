class Solution:
	# Naive solution would be: O(N^2), searching all two points, which separates leftSum, midSum and rightSum
	# O(NlogN)
	def waysToSplit(self, nums: List[int]) -> int:
		def findLeft(A, i, target):
			l, r = i + 1, len(A) - 2

			while l < r:
				mid = (l + r) // 2
				if A[mid] < target:
					l = mid + 1
				else:
					r = mid

			return l if A[l] >= target else -1

		def findRight(A, i, target):
			l, r = i + 1, len(A) - 2
			while l < r:
				mid = (l + r + 1) // 2
				if A[mid] > target:
					r = mid - 1
				else:
					l = mid

			return l if A[l] <= target else -1

		n = len(nums)
		A = [0] * n

		# prefix sum array
		A[0] = nums[0]

		for i in range(1, n):
			A[i] = A[i - 1] + nums[i]

		res = 0

		# [i+1, j] is the middle sub array:  A[i] <= A[j] - A[i] <= A[N-1] - A[j]
		# So, A[i] <= A[j] - A[i] -> A[j] >= 2 * A[i]
		#                            A[j] <= (A[N-1] + A[i]) // 2

		# j has left boundary and right boundary
		for i in range(n - 2):
			# for each i split array from [0, i], [i+1, left], [left+1, N-1], to [0, i], [i+1, right], [right, N-1].
			left = findLeft(A, i, A[i] * 2)
			right = findRight(A, i, (A[i] + A[-1]) // 2)
			if left > -1 and right > -1:  # both left and right are qualified boundary, so total right- left + 1 possible splits
				res += max(0, right - left + 1)
		return res % 1_000_000_007
