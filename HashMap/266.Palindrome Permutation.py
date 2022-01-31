import collections


class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        cnt = collections.Counter(s)
        odd = 0
        for c, fre in cnt.items():
            if fre % 2 == 1:
                if odd == 1:
                    return False
                else:
                    odd += 1

        return True