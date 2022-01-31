'''
You need to find some sequence from 0th index which is in increasing order, let this sequence a_1 <= a_2 <= ... <= a_i
Then you need to find some sequence from the back which is in decreasing order such that b_j <= b_(j+1) <= ... <= b_n (j <= i)

Then it is guranteed you need to remove subarray from (i + 1, j - 1).
But it is possible if we could merge some part from b_j <= b_(j+1) <= ... <= b_n, with a_1 <= a_2 <= ... <= a_i, to create a bigger increasing subarray.

'''

class Solution:
	def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
		n = len(arr)
		l = 0
		r = n - 1

		while l + 1 < n and arr[l] <= arr[l + 1]:
			l += 1
		if l == n - 1:
			return 0

		while r - 1 > 0 and arr[r - 1] <= arr[r]:
			r -= 1

		res = min(n - l - 1, r)

		j = r
		for i in range(l + 1):  # i is left pointer:
			while j < n and arr[i] > arr[j]:
				j += 1

			if j == n:
				break

			# s[i+1, j] can be removed
			res = min(res, j - i - 1)

		return res