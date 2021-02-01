import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #         if not matrix or not matrix[0]:
        #             return -1
        #         n = len(matrix)
        #         a = []
        #         for i in range (n):
        #             for j in range (n):
        #                 heapq.heappush(a, matrix[i][j])
        #         print(a)
        #         while k > 0:
        #             res = heapq.heappop(a)
        #             k -= 1

        #         return res

        if not matrix or not matrix[0]:
            return -1
        n = len(matrix)

        l, r = matrix[0][0], matrix[n - 1][n - 1]

        while l < r:
            mid = (l + r) // 2
            count = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        count += 1

            if count < k:
                l = mid + 1
            else:
                r = mid
        return l
