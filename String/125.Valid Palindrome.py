class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        lst = list(s)
        filtered = list(filter(lambda x: x.isalnum(), lst))
        filtered = [i.lower() for i in filtered]
        return filtered == filtered[::-1]
