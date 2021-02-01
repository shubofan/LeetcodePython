from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = set()

        res = set()

        if len(s) < 10:
            return res

        for i in range(len(s) - 9):
            se = s[i: i + 10]

            if se not in seq:
                seq.add(se)
            else:
                res.add(se)
        return list(res)