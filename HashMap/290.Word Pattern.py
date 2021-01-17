import heapq


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic1 = defaultdict(list)
        dic2 = defaultdict(list)

        lst = s.split(' ')
        if len(pattern) != len(lst):
            return False

        for i in range(len(pattern)):
            dic1[pattern[i]] += [i]
            dic2[lst[i]] += [i]
        for vals in dic1.values():
            if vals not in dic2.values():
                return False
        return True
