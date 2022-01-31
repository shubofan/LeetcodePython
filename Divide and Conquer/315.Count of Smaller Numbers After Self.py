from typing import List
# Time：O(NlogN), it is actually a merge sort, which took O(NlogN)
# Space：O(N)，3 lists needed 一个lst for (idx, num)，一个tem list，a lst of res

class Solution:
    # 数组中的逆序对 https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # list of tuple (index, value)
        lst = [(v, index) for index, v in enumerate(nums)]
        self.res = [0] * n
        self.mergeSort(lst)
        return self.res

    def mergeSort(self, lst: List[int]) ->  List[int]:
        n = len(lst)

        if n > 1:
            l = self.mergeSort(lst[:n // 2])
            r = self.mergeSort(lst[n // 2:])
            return self.merge(l, r)
        return lst

    # l, r are sorted array from large to small like [5,2], [6,1]
    def merge(self, l: List[int], r: List[int]) -> List[int]:
        tem = []
        i, j = 0, 0

        while i < len(l) and j < len(r):
            # current element in left array is less than current value in right array
            if l[i][0] > r[j][0]:
                self.res[l[i][1]] += len(r) - j
                tem += [l[i]]
                i += 1
            else:
                tem += [r[j]]
                j += 1
        # remaining elements in left array
        while i < len(l):
            tem += [l[i]]
            i += 1
        while j < len(r):
            tem += [r[j]]
            j += 1
        return tem


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lst = [(num, idx) for idx, num in enumerate(nums)]

        n = len(nums)
        res = [0] * n

        def mergeSort(lst):
            if len(lst) == 1:
                return lst

            l_lst = mergeSort(lst[:len(lst) // 2])
            r_lst = mergeSort(lst[len(lst) // 2:])

            return merge(l_lst, r_lst)

        # sorted arr from large to small like [5,2], [6,1]
        def merge(l_lst, r_lst):
            tem = []

            l, r = 0, 0

            while l < len(l_lst) and r < len(r_lst):

                if l_lst[l][0] > r_lst[r][0]:
                    res[l_lst[l][1]] += (len(r_lst) - r)

                    tem += [l_lst[l]]
                    l += 1
                else:
                    tem += [r_lst[r]]
                    r += 1

            while l < len(l_lst):
                tem += [l_lst[l]]
                l += 1

            while r < len(r_lst):
                tem += [r_lst[r]]
                r += 1
            return tem

        mergeSort(lst)
        return res