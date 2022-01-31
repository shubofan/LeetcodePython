from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        # sorted descendingly by first element（height） then asendingly by 2nd element
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        for p in people:
            if not res:
                res += [p]
            else:
                res.insert(p[1], p)
        return res

