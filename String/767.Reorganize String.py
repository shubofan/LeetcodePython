class Solution:
    def reorganizeString(self, s: str) -> str:
        A = []
        N = len(s)
        for c, x in sorted((s.count(x), x) for x in set(s)):
            if c > (N + 1) / 2:
                return ""
            A.extend(c * x)

        res = [None] * N

        l1 = 0
        l2 = N // 2
        while l2 < N:
            res[l1] = A[l2]
            l1 += 2
            l2 += 1

        l1 = 1
        l2 = 0
        while l2 < N // 2:
            res[l1] = A[l2]
            l1 += 2
            l2 += 1

        return "".join(res)
