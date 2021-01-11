from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] - mid - 1 >= k:
                r = mid
            else:
                l = mid + 1

        # like arr = [2,3,4,7,11], k = 5, the missing element is in the original arr, so index should start from l
        if arr[l] - l - 1 >= k:
            return l + k
        # like [1,2,3,4] 2, the missing element is not in the original arr, so index short start from l + 1
        else:
            return l + 1 + k