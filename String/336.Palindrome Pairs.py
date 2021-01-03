class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        dic = {}

        for idx, word in enumerate(words):
            dic[word[::-1]] = idx

        for idx, word in enumerate(words):
            size = len(word)
            # if word itself is a palindrome, check if '' is found
            if word and word[::-1] == word and '' in dic:
                res += [[dic[''], idx]]

            for i in range(size):
                s1 = word[:i]
                s2 = word[i:]

                # if right is palindrome, dic[s1] + right is palindrome
                if s2 == s2[::-1]:
                    if s1 in dic and dic[s1] != idx:
                        res += [[idx, dic[s1]]]

                # if left is palindrome, left + dic[s2] is palindrome
                if s1 == s1[::-1]:
                    if s2 in dic and dic[s2] != idx:
                        res += [[dic[s2], idx]]
        return res
