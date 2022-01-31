class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
        c = collections.Counter(ages)
        # return sum(request(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)
        res = 0
        for a in c:
            for b in c:
                if request(a, b):
                    res += c[a] * c[b]
                    if a == b:
                        res -= c[b]
        return res