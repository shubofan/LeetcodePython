class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum1 = {}
        res = 0

        for i in range(len(A)):
            for j in range(len(B)):
                sum1[A[i] + B[j]] = sum1.get(A[i] + B[j], 0) + 1

        for i in range(len(C)):
            for j in range(len(D)):
                if (C[i] + D[j]) * -1 in sum1:
                    res += sum1.get((C[i] + D[j]) * -1)
        return res