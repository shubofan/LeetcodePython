import heapq


class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     pq = []
    #     for i in range(len(nums1)):
    #         for j in range(len(nums2)):
    #             heapq.heappush(pq, ((nums1[i] + nums2[j]) * - 1, [nums1[i], nums2[j]]))
    #             if len(pq) > k:
    #                 heapq.heappop(pq)
    #     res = []
    #     # print(pq)
    #     while pq:
    #         res += [heapq.heappop(pq)[1]]
    #     res.reverse()
    #     return res

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        if not nums1 or not nums2:
            return []
        # (indexInNums1, indexInNums2)
        # push (0, 0), (1, 0) ..... (len(nums1) - 1, 0) to the heap
        for i in range(len(nums1)):
            heapq.heappush(pq, (nums1[i] + nums2[0], [i, 0]))  # O(mlgm)

        res = []

        while pq and k > 0:
            _, pair = heapq.heappop(pq)  # O(lgk) -> constant
            idx1, idx2 = pair[0], pair[1]

            res += [[nums1[idx1], nums2[idx2]]]
            # push(idx1, idx2 + 1) to heap since heap(idx1, idx2) has been selected
            if idx2 < len(nums2) - 1:
                idx2 += 1
                heapq.heappush(pq, (nums1[idx1] + nums2[idx2], [idx1, idx2]))  # O(lgk) -> constant
            k -= 1

        return res
