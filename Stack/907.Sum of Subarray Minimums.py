class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        l = [1] * n  # l[i]: count of elements >= arr[i] and upto the left of i
        r = [1] * n  # r[i]: count of elements > arr[i] and upto the right of i
        stack = []

        # a monotone increase stack: A tuple in stack (arr[i], count of element<= arr[i] at the left of i)
        for i in range(len(arr)):
            # pop all the element that value >= arr[i], get sum
            while stack and stack[-1][0] >= arr[i]:
                l[i] += stack.pop()[1]
            stack += [(arr[i], l[i])] # count of elements >= arr[i]

        stack = []
        # a monotone increase stack: A tuple in stack (arr[i], count of element< arr[i] at the right of i)
        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1][0] > arr[i]:
                r[i] += stack.pop()[1]
            stack += [(arr[i], r[i])]

        res = 0

        # for each arr[i], get total number of sub-arrays where arr[i] is the min element
        for i in range(n):
            res += l[i] * r[i] * arr[i]  # l[i] * r[i] is total number of sub-arrays where arr[i] is the min element
        return res % (10 ** 9 + 7)

