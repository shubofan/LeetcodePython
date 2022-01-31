from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        if len(s) < 4 or len(s) > 12:
            return self.res
        self.helper(s, 0, [])
        return self.res

    def helper(self, s: str, start: int, ip: List[str]):
        if len(ip) == 4 and start == len(s):
            self.res += ['.'.join(ip)]
            return
        if len(ip) > 4:
            return
        for i in range(start + 1, len(s) + 1):
            segment = s[start:i]
            if (0 < int(segment) <= 255 and segment[0] != '0') or (int(segment) == 0 and len(segment) == 1):
                ip += [segment]
                self.helper(s, i, ip)
                ip.pop()
