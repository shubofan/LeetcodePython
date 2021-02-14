from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l, r = 0, 0
        re_write = 0
        while r < n:
            while r < n and chars[l] == chars[r]:
                r += 1
            size = r - l

            chars[re_write] = chars[l]
            re_write += 1
            if size > 1:
                for i in range(len(str(size))):
                    chars[re_write] = str(size)[i]
                    re_write += 1
            l = r
        return re_write
