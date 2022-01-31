class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		nums.sort()
		for i in range(len(nums) - 1):
			if nums[i] == nums[i + 1]:
				return nums[i]

		return -1

	# Time O(nlogn)
	# Time O(nlogn)
class Solution:
	def findDuplicate(self, nums):
		n = len(nums)
		l, r = 1, n

		while l < r:
			mid = (l + r) // 2
			cnt = 0
			for num in nums:
				if num <= mid:
					cnt += 1
			if cnt <= mid:
				l = mid + 1
			else:
				r = mid
		return l


# Time complexity : O(n)
# Space complexity : O(1)

class Solution:
	def findDuplicate(self, nums):
		# Find the intersection point of the two runners.
		fast = slow = nums[0]
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break

		# Find the "entrance" to the cycle.
		slow = nums[0]
		while slow != fast:
			fast = nums[fast]
			slow = nums[slow]

		return fast