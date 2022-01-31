# O (N^2)
# class Solution:
#     def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
#         # i is the start index of 1st sub-array
#         i, n, res = 0, len(nums), 0

#         A = [0] * (n + 1)

#         for k in range(1, n+1):
#             A[k] = nums[k-1] + A[k-1]
#         # A[j] - A[i] = nums[i:j]

#         # assume that 1st sub-array has length of firstLen
#         while i + firstLen < n + 1:
#             r = i + firstLen
#             first_sum = A[r] - A[i] # nums[i:r]
#             j = r # j is the start index of 2nd sub-array
#             while j + secondLen < n + 1:
#                 second_sum = A[j + secondLen] - A[j] # nums[r: r+secondLen]
#                 j += 1
#                 res = max(res, first_sum + second_sum)
#             i += 1

#         i = 0
#         # assume that 1st sub-array has length of secondLen
#         while i + secondLen < n + 1:
#             r = i + secondLen
#             second_sum = A[r] - A[i]
#             j = r
#             while j + firstLen < n + 1:
#                 # print(second_sum)
#                 first_sum = A[j + firstLen] - A[j]
#                 j += 1
#                 res = max(res, first_sum + second_sum)
#             i += 1

#         return res


# Slide window, O(N) time
class Solution:
	def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:

		n = len(nums)
		A = [0] * (n + 1)

		for k in range(1, n + 1):
			A[k] = nums[k - 1] + A[k - 1]
		# A[j] - A[i] = nums[i:j]

		max_first = A[firstLen]
		max_second = A[secondLen]
		res = A[firstLen + secondLen]

		# i代表当前位于右边的数组的末尾索引
		for i in range(firstLen + secondLen + 1, n + 1):
			# 1st,2nd i代表2nd的最后一个索引, 此时2nd已确定
			cur_second = A[i] - A[i - secondLen]

			# max_first, max first sub_string before 2nd
			max_first = max(max_first, A[i - secondLen] - A[i - firstLen - secondLen])

			# sum of 1st, 2nd
			res_first_second = max_first + cur_second

			# 2nd,1st, i代表1st的最后一个索引,此时1st已确定
			cur_first = A[i] - A[i - firstLen]

			# max_second, max 2nd sub_string before 1st
			max_second = max(max_second, A[i - firstLen] - A[i - firstLen - secondLen])

			# sum of 2nd, 1st
			res_second_first = max_second + cur_first
			res = max(res, res_first_second, res_second_first)
		return res



