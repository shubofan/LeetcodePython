import collections
from typing import List


class Solution:
    # Time: O(2**N) where N is the number of parentheses. For each parenthesis, we either keep it or discard it,
    # so there will be 2**N possible combinations

    #
    #     def removeInvalidParentheses(self, s: str) -> List[str]:
    #         # open Parentheses to be removed
    #         open_to_be_removed = 0
    #         # close Parentheses to be removed
    #         close_to_be_removed = 0
    #         self.res = set()
    #         for c in s:
    #             if c == '(':
    #                 open_to_be_removed += 1
    #             if c == ')':
    #                 if open_to_be_removed > 0:
    #                     open_to_be_removed -= 1
    #                 else:
    #                     close_to_be_removed += 1
    #         self.remove(s,0,0,0,open_to_be_removed, close_to_be_removed, '')
    #         return list(self.res)

    #     def remove(self, s, idx, open_count, close_count,open_to_be_removed, close_to_be_removed, path):
    #         # path is a valid Parentheses expression
    #         if idx == len(s):
    #             if open_to_be_removed == close_to_be_removed == 0:
    #                 self.res.add(path)
    #             return
    #         # if open_to_be_removed > 0, so remove '('
    #         if s[idx] == '(' and open_to_be_removed > 0:
    #             self.remove(s, idx + 1, open_count, close_count, open_to_be_removed -1, close_to_be_removed, path)
    #         # if close_to_be_removed > 0, so remove '('
    #         if s[idx] == ')' and close_to_be_removed > 0:
    #             self.remove(s, idx + 1, open_count, close_count, open_to_be_removed, close_to_be_removed - 1, path)
    #         # just add it to path for any other letter
    #         if s[idx] not in '()':
    #             self.remove(s, idx + 1, open_count, close_count, open_to_be_removed, close_to_be_removed, path+s[idx])
    #         # If the current parenthesis is an opening Parentheses, we consider it
    #         # and increment left and  move forward
    #         if s[idx] == '(':
    #             self.remove(s, idx + 1, open_count + 1, close_count, open_to_be_removed, close_to_be_removed, path+'(')
    #         # For closing Parentheses in its count < open_count, we are ok to add in to path
    #         if s[idx] == ')' and close_count < open_count:
    #             self.remove(s, idx + 1, open_count, close_count + 1, open_to_be_removed, close_to_be_removed, path+')')

    # BFS

    """
    T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = collections.deque()
        q += [s]
        res = []
        while q:
            # check if any expression in current q is valid or not
            for cur in q:
                if self.isValid(cur):
                    res += [cur]

            # As long as fount one or some in res, it must have max length, so just stop
            if res:
                return res

            # if all the expressions are not valid, for each of which, remove more
            s = set()
            for i in range(len(q)):
                cur = q[i]
                for j in range(len(cur)):
                    if cur[j] in '()':
                        new_s = cur[:j] + cur[j + 1:]
                        s.add(new_s)

            q = collections.deque(s)

        return res

    def isValid(self, s):
        pair = 0
        for c in s:
            if c == '(':
                pair += 1
            if c == ')':
                pair -= 1
            if pair < 0:
                return False
        return pair == 0