class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(' ')
        lst = s.split(' ')
        lst.reverse()
        r = filter(lambda x: x != '', lst)
        return ' '.join(r)
