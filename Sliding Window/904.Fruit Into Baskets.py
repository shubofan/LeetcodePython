import collections
from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        res = 0
        # Space O(1) , cnt most 3 keys
        cnt = collections.defaultdict(int)

        l, r = 0, 0
        # Time o(n), each element will be put into map and pop from map
        while r < n:
            cnt[tree[r]] += 1
            while len(cnt) > 2:
                cnt[tree[l]] -= 1
                if cnt[tree[l]] == 0:
                    cnt.pop(tree[l])

                l += 1
            res = max(res, r - l + 1)
            r += 1

        return res