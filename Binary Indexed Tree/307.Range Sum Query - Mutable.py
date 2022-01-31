from typing import List


class NumArray:

	# self.c[1] = nums[0] # lowbit (1) = 1

	# self.c[2] = nums[0] + nums[1] # lowbit (1) = 1

	# self.c[3] = nums[2]

	# self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]

	# self.c[5] = nums[4]

	# self.c[6] = nums[4] + nums[5]

	# self.c[7] = nums[6]

	# self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]

	def __init__(self, nums: List[int]):
		self.nums = nums
		self.bit = [0] * (len(nums) + 1)

		for i in range(len(nums)):
			k = i + 1
			while k < len(self.bit):
				self.bit[k] += nums[i]
				k += k & (-k)

	def update(self, index: int, val: int) -> None:
		diff = val - self.nums[index]
		self.nums[index] = val
		k = index + 1
		# each time remove a bit 0 from end, so total take O(log(n))
		while k < len(self.bit):
			self.bit[k] += diff
			k += (k & -k)

	def sumRange(self, left: int, right: int) -> int:

		right += 1
		res = 0
		# first get sum of [0:right] = res
		# Similarly, take O(log(n))
		while right > 0:
			res += self.bit[right]
			right -= (right & -right)

		# res - sum of [0:left-1], so the remaining is the sum of [left:right]
		while left > 0:
			res -= self.bit[left]
			left -= (left & -left)
		return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)