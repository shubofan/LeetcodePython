from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1
        even = 0
        n = len(A)
        while odd < n and even < n:
            while even < len(A) and A[even] % 2 == 0:
                even += 2
            while odd < len(A) and A[odd] % 2 != 0:
                odd += 2
            if odd < n and even < n:
                A[even], A[odd] = A[odd], A[even]
        return A
