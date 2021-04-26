from typing import List


class Solution:
    # 数组中的逆序对 https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/shu-zu-zhong-de-ni-xu-dui-by-leetcode-solution/
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # list of tuple (index, value)
        lst = [(v, index) for index, v in enumerate(nums)]
        self.res = [0] * n
        self.mergeSort(lst)
        return self.res

    def mergeSort(self, lst: List[int]) -> None:
        n = len(lst)

        if n > 1:
            l = self.mergeSort(lst[:n // 2])
            r = self.mergeSort(lst[n // 2:])
            return self.merge(l, r)
        return lst

    # l, r are 2 sorted arraies
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
            # self.res[l[i][1]] += len(r) - j  len(r) -j = 0 so can be commented
            tem += [l[i]]
            i += 1
        while j < len(r):
            tem += [r[j]]
            j += 1
        return tem
