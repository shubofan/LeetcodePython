from typing import List


class Solution:
    """
    Building further on this idea, we can observe that a + b == -(c + d) .
    First, we will count sums of elements a + b from the first two arrays using a hashmap.
    Then, we will enumerate elements from the third and fourth arrays, and search for a complementary sum a + b == -(c + d) in the hashmap.
    """
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum1 = {} # <sum, fre>
        res = 0

        """
        Time Complexity:(n^2)We have 2 nested loops to count sums, and another 2 nested loops to find complements.

        Space Complexity"(n^2)for the hashmap. There could be up to (n^2) distinct a + b keys. 
        
        """

        for i in range(len(A)):
            for j in range(len(B)):
                sum1[A[i] + B[j]] = sum1.get(A[i] + B[j], 0) + 1

        for i in range(len(C)):
            for j in range(len(D)):
                if (C[i] + D[j]) * -1 in sum1:
                    res += sum1.get((C[i] + D[j]) * -1)
        return res