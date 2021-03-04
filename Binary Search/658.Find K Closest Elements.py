class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right, pos = 0, len(arr) - 1, 0

        while left <= right:
            mid = left + (right - left) // 2
            if (arr[mid] == x):
                pos = mid
                break
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        pos = right

        left, right = max(0, pos - k), min(pos + k, len(arr) - 1)
        # shrink [pos - k, pos + k]
        while right - left + 1 > k:
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
        return arr[left: right + 1]

    # l is the position where new array starts from
#         l , r = 0, len(arr) - k
#         while l < r :
#             mid = (l + r) // 2
#             if x - arr[mid] >  arr[mid + k] - x:
#                 l = mid + 1
#             else:
#                 r = mid

#         return arr[l : r + k]