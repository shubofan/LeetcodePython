from heapq import *

# O(klogk)
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        pq = []

        res = []
        for arr_idx, array in enumerate(arrays):
            if array:
                heappush(pq, (array[0], arr_idx, 0))

        while pq:

            val, arr_idx, idx = heappop(pq)
            res += [val]

            if idx + 1 < len(arrays[arr_idx]):
                heappush(pq, (arrays[arr_idx][idx+1], arr_idx, idx+1))

        return res

    def mergekSortedArrays(self, arrays):
        def split(arrays):
            if len(arrays) == 1:
                return arrays[0]
            mid = len(arrays) // 2

            left = split(arrays[:mid])
            right = split(arrays[mid:])

            return merge(left, right)

        def merge(left, right):
            i, j = 0, 0
            m, n = len(left), len(right)
            res = []
            while i < m and j < n:
                if left[i] <= right[j]:
                    res += [left[i]]
                    i += 1
                else:
                    res += [right[j]]
                    j += 1

            while i < m:
                res += [left[i]]
                i += 1

            while j < n:
                res += [right[j]]
                j += 1

            return res

        return split(arrays)
