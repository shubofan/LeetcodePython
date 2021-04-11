from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        l , r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                r = mid
        if ord(letters[l]) >ord(target):
            return letters[l]
        else:
            return letters[0]