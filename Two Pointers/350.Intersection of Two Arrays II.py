import collections
from typing import List


class Solution:
	# Time (O max(m, n))
	# Space (O (m + n))
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
	    c1, c2 = collections.Counter(nums1), collections.Counter(nums2)
	    if len(c1) > len(c2):
	        self.intersect(c2, c1)
	    res = []
	    for num, fre in c2.items():
	        fre = min(c1[num], fre)
	        res.extend([num] * fre)
	    return res

	# Time: O(max(nlogn ,mlogm, n+m))
	# Space: O(1)
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		nums1.sort()
		nums2.sort()
		l1, l2 = len(nums1), len(nums2)
		i, j = 0, 0
		res = []
		while i < l1 and j < l2:
			if nums1[i] < nums2[j]:
				i += 1
			elif nums1[i] > nums2[j]:
				j += 1
			else:
				res += [nums1[i]]
				i += 1
				j += 1
		return res

#     Follow-up Questions:

#     What if the given array is already sorted? How would you optimize your algorithm?
#         We can use either Approach 2.  It will give us linear time and constant memory complexity.

#     What if nums1's size is small compared to nums2's size? Which algorithm is better?
#         Approach 1 is a good choice here as we use a hash map for the smaller array.

#     What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

#         * If nums1 fits into the memory:
#             We can use Approach 1 to collect counts for nums1 into a hash map. Then, we can sequentially load and process nums2.

#         * If neither of the arrays fit into the memory, we can apply some partial processing strategies:

#             Data sharding: Split the numeric range into sub-ranges that fits into the memory. Modify Approach 1 to collect counts only within a given subrange, and call the method multiple times (for each subrange).

#             Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.
