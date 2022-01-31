from typing import List


class Solution:
	def reversePairs(self, nums: List[int]) -> int:
		self.cnt = 0
		self.merge_sort(nums, 0, len(nums) - 1)

		return self.cnt

	#  时间复杂度：O(NlogN)，其中 N 为数组的长度。
	#  空间复杂度：O(N)，其中 N 为数组的长度。

	def merge_sort(self, nums: List[int], l: int, r: int) -> int:
		if l >= r:
			return 0
		mid = (l + r) // 2

		self.merge_sort(nums, l, mid)
		self.merge_sort(nums, mid + 1, r)
		self.merge(nums, l, mid, r)

	def merge(self, nums: List[int], l: int, mid: int, r: int) -> int:
		tem = []

		# count reverse pairs in nums[l:r+1]
		i, j = l, mid + 1
		while i <= mid and j <= r:
			if nums[i] <= 2 * nums[j]:
				i += 1
			else:
				self.cnt += (mid - i + 1)
				j += 1


		# sort nums[l:r+1]
		i, j = l, mid + 1
		while i <= mid and j <= r:
			if nums[i] <= nums[j]:
				tem += [nums[i]]
				i += 1
			else:
				tem += [nums[j]]
				j += 1
		while i <= mid:
			tem += [nums[i]]
			i += 1

		while j <= r:
			tem += [nums[j]]
			j += 1

		for i in range(len(tem)):
			nums[l + i] = tem[i]
