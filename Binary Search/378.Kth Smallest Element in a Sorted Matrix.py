import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])

        l, r = matrix[0][0], matrix[m - 1][n - 1]

        # overall time complexity: O(N×log(r−l)) where N is the number of element in the matrix

        # total log(r−l) times binary search, and each binary search take O(N)

        while l < r:
            mid = (l + r) // 2
            cnt = 0
            x, y = m - 1, 0

            # Find total elements in the matrix <= mid: Take O(N)
            # start from matrix[m-1][0] -> left corner
            # if matrix[x][y] <= mid, entire column <= mid, cnt += x + 1, then move to right
            # move to up
            while x >= 0 and y < n:
                if matrix[x][y] <= mid:
                    cnt += x + 1
                    y += 1
                else:
                    x -= 1

            if cnt < k:
                l = mid + 1
            else:
                r = mid
        return l




# Time Complexity: let X=min(K,N); O(X*Log(X)) + O(K*log(X)), since X <= K -> total time complexity: K*log(X)
#
# Well the heap construction takes O(X*Log(X)) time.
# After that, we perform K
# iterations and each iteration has two operations. We extract the minimum element from a heap containing X elements.
# Then we add a new element to this heap. Both the operations will take O(log(X)) time.

# Thus, the total time complexity for this algorithm comes down to be O(X+Klog(X))
# where X is min(K,N).

# Space Complexity: O(X)
# which is occupied by the heap.


# treat each row as a list
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
                if not matrix or not matrix[0]:
                    return -1
                n = len(matrix)
                pq = []
                for i in range (min(k, n)):
                    heapq.heappush(pq, (matrix[i][0], i, 0))

                val = 0
                while k > 0:
                    val, row, col = heapq.heappop(pq)
                    if col + 1 < len(matrix[row]):
                        heapq.heappush(pq, (matrix[row][col+1], row, col+1))

                    k -= 1

                return val
