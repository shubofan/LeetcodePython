from typing import List


#Time Complexity: O(N), where N is the number of elements in the array.
# In worst case we might end up visiting every element of array TWICE, once by left pointer and once by right pointer.

# Space Complexity: O(1). We do not use any extra space.

class Solution:
	def longestOnes(self, nums: List[int], k: int) -> int:
		l = 0
		n = len(nums)

		zeros = 0
		res = 0
		for r in range(n):
			if nums[r] == 0:
				zeros += 1
			while zeros > k:
				if nums[l] == 0:
					zeros -= 1
				l += 1
			res = max(res, r - l + 1)
		return res