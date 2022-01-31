class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		#         res = []
		#         l1 , l2 = 0, 0
		#         m , n = len(nums1), len(nums2)
		#         while l1 < m and l2 < n:
		#             if nums1[l1] < nums2[l2]:
		#                 res += [nums1[l1]]
		#                 l1 += 1
		#             else:
		#                 res += [nums2[l2]]
		#                 l2 += 1

		#         while l1 < m:
		#             res += [nums1[l1]]
		#             l1 += 1

		#         while l2 < n:
		#             res += [nums2[l2]]
		#             l2 += 1

		#         if len(res) % 2 == 1:
		#             idx = len(res) // 2
		#             return res[idx]
		#         else:
		#             idx1, idx2 = len(res) // 2 - 1, len(res) // 2
		# return (res[idx1] +  res[idx2]) / 2.0

		if len(nums1) > len(nums2):
			nums1, nums2 = nums2, nums1

		m, n = len(nums1), len(nums2)

		total_left = (m + n + 1) // 2

		# 在 nums1 的区间 [0, m] 里查找恰当的分割线，
		# 使得 nums1[i - 1] <= nums2[j] && nums2[j - 1] <= nums1[i]
		l, r = 0, m
		while l < r:
			i = (l + r + 1) // 2  # position of first element after split line in nums1
			j = total_left - i  # position of first element after split line in nums2
			if nums1[i - 1] > nums2[j]:
				r = i - 1
			else:
				l = i

		# 当数组的总长度为偶数的时候，中位数就是分割线左边的最大值与分割线右边的最小值的平均数；
		# 当数组的总长度为奇数的时候，中位数就是分割线左边的最大值。因此，在数组长度是奇数的时候，中位数就是分割线左边的所有数的最大值
		i = l
		j = total_left - l
		nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
		nums1_right_min = float('inf') if i == m else nums1[i]

		nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
		nums2_right_min = float('inf') if j == n else nums2[j]

		if (m + n) % 2 == 1:
			return max(nums1_left_max, nums2_left_max)
		else:
			return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
