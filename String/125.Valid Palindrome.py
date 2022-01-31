class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        lst = list(s)
        filtered = list(filter(lambda x: x.isalnum(), lst))
        filtered = [i.lower() for i in filtered]
        return filtered == filtered[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l] or not s[l].isalnum():
                l += 1

            elif not s[r] or not s[r].isalnum():
                r -= 1

            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1

        return True